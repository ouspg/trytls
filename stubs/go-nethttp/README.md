# Go stub for TryTLS project

## How to run

1. Install

    ```shell
        go get github.com/ouspg/trytls/stubs/go-nethttp
    ```

2. Run

    ```shell
        $GOPATH/bin/go-nethttp https://www.example.com/ 443
    ```

## Test result

| TLS verification result     | Exit code |
| ----------------------------| --------- |
| SUCCESS/FAILURE             | 0         |
| ERROR                       | 1         |

More information about error may be available on standard output.

## Alternative: local development

Simply call `go run run.go https://www.example.com/` to compile and run this
stub in one go. For performance you will want to `go build` a binary first
though.

Example:

```shell
$ go run run.go https://badssl.com/
VERIFY SUCCESS
$ go run run.go https://untrusted-root.badssl.com/
VERIFY FAILURE
```

# Dependencies:

To build, [Go 1.6 or newer][go] with a [properly configured GOPATH][GOPATH].
The resulting binary does not depend on Go tools being installed, but is
platform specific. [Cross-platform building][GOOS] is easy.


[go]: https://golang.org/ "The Go Programming Language"
[GOPATH]: https://golang.org/doc/code.html#GOPATH "How to Write Go Code - The GOPATH environment variable"
[GOOS]: https://github.com/golang/go/wiki/WindowsCrossCompiling
