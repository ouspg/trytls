package main

import (
	"crypto/tls"
	"crypto/x509"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
)

func main() {
	if len(os.Args) < 3 || len(os.Args) > 4 {
		fmt.Printf("usage: %v <host> <port> [cafile]\n", os.Args[0])
		os.Exit(1)
	}

	client := http.DefaultClient
	if len(os.Args) == 4 {
		cadata, err := ioutil.ReadFile(os.Args[3])
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}

		pool := x509.NewCertPool()
		if !pool.AppendCertsFromPEM(cadata) {
			fmt.Println("Couldn't append certs")
			os.Exit(1)
		}

		client = &http.Client{
			Transport: &http.Transport{
				TLSClientConfig: &tls.Config{RootCAs: pool},
			},
		}
	}

	// Perform an HTTPS Request
	_, err := client.Get("https://" + os.Args[1] + ":" + os.Args[2])
	if err != nil {
		fatalError := strings.Contains(err.Error(), "no such host")
		fmt.Println(err.Error())
		if fatalError {
			os.Exit(1)
		}
		fmt.Println("REJECT")
	} else {
		fmt.Println("ACCEPT")
	}
	os.Exit(0)
}
