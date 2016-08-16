package main

import (
	"fmt"
	"net/http"
	"os"
	"strings"
)

func main() {
	if len(os.Args) == 4 {
		fmt.Println("UNSUPPORTED")
		os.Exit(0)
	} else if len(os.Args) != 3 {
		fmt.Printf("usage: %v <host> <port>\n", os.Args[0])
		os.Exit(1)
	}

	url := "https://" + os.Args[1] + ":" + os.Args[2]

	// Perform a HTTP(s) Request
	_, err := http.Get(url)
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
