package main

import (
	"fmt"
	"net/http"
	"os"
	"strings"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("UNSUPPORTED")
		os.Exit(1)
	}

	url := "https://" + os.Args[1]

	// Perform a HTTP(s) Request
	_, err := http.Get(url)
	if err != nil {
		sslError := strings.Contains(err.Error(), "certificate") || strings.Contains(err.Error(), "handshake")
		if sslError {
			fmt.Println("VERIFY FAILURE")
		} else {
			fmt.Println(err)
		}
		os.Exit(1)
	}
	fmt.Println("VERIFY SUCCESS")
	os.Exit(0)
}
