package main

import (
	"crypto/tls"
	"crypto/x509"
	"errors"
	"flag"
	"fmt"
	"io/ioutil"
	"net"
	"net/http"
	"net/url"
	"os"
	"time"
)

var timeout = flag.Duration("timeout", 5*time.Second, "HTTP request timeout (ms)")

func main() {
	flag.Parse()
	var host, port, caFileName string
	switch len(flag.Args()) {
	case 3:
		caFileName = flag.Arg(2)
		fallthrough
	case 2:
		host = flag.Arg(0)
		port = flag.Arg(1)
	default:
		fmt.Printf("usage: %v <host> <port> [cafile]\n", os.Args[0])
		os.Exit(1)
	}

	if err := checkTLS(host, port, caFileName); err != nil {
		fmt.Println("FATAL:", err)
		os.Exit(1)
	}
}

func checkTLS(host, port, caFileName string) error {
	client := &http.Client{
		Timeout: *timeout,
	}

	if caFileName != "" {
		roots, err := loadRootCA(caFileName)
		if err != nil {
			return err
		}
		client.Transport = &http.Transport{
			TLSClientConfig: &tls.Config{RootCAs: roots},
		}
	}

	uri := "https://" + net.JoinHostPort(host, port)
	if _, err := client.Get(uri); err != nil {
		// Timeouts are fatal without verdict
		if timeouterr, ok := err.(timeouter); ok {
			if timeouterr.Timeout() {
				return err
			}
		}
		// Connection errors from dialer are fatal without verdict
		if urlerr, ok := err.(*url.Error); ok {
			if operr, ok := urlerr.Err.(*net.OpError); ok {
				if operr.Op == "dial" {
					return err
				}
			}
		}

		fmt.Println(err.Error())
		fmt.Println("REJECT")
		return nil
	}
	fmt.Println("ACCEPT")
	return nil
}

type timeouter interface {
	Timeout() bool
}

func loadRootCA(fileName string) (roots *x509.CertPool, err error) {
	cadata, err := ioutil.ReadFile(fileName)
	if err != nil {
		return
	}
	roots = x509.NewCertPool()
	if ok := roots.AppendCertsFromPEM(cadata); !ok {
		return nil, errors.New("failed to parse CA file")
	}
	return roots, nil
}
