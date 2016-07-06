package main

import (
	"fmt"
	"net/http"
	"os"
	"strings"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Println("UNSUPPORTED")
		os.Exit(1)
	}

	url := "https://" + os.Args[1] + ":" + os.Args[2]

	// Perform a HTTP(s) Request
	_, err := http.Get(url)
	if err != nil {
		sslError := strings.Contains(err.Error(), "certificate") || strings.Contains(err.Error(), "handshake")
		if sslError {
			fmt.Println("VERIFY FAILURE")
			os.Exit(0)
		} 
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println("VERIFY SUCCESS")
	os.Exit(0)
}
