package main

import (
	"fmt"
	"net/http"
	"os"
)

func usage() {
	fmt.Printf("Usage: %v <URL>", os.Args[0])
}

func main() {
	if len(os.Args) != 2 {
		usage()
		return
	}
	url := os.Args[1]

	// Perform a HTTP Request
	_, err := http.Get(url)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	fmt.Println("TLS verification OK")
}
