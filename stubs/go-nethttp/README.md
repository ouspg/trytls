# Go stub for TryTLS project

## How to run

1. Install

    ```shell
        go get github.com/ouspg/trytls/stubs/go-nethttp
    ```

2. Run

    ```shell
        $GOPATH/bin/go-nethttp example.com 443
    ```

## Test result

| TLS verification result     | Exit code |
| ----------------------------| --------- |
| SUCCESS/FAILURE             | 0         |
| ERROR                       | 1         |

More information about error may be available on standard output.

## Alternative: local development

Usage:

```shell
$ go build
$ ./go-nethttp badssl.com 443
ACCEPT
$ ./go-nethttp untrusted-root.badssl.com 443
REJECT
```

# Dependencies:

To build, [Go 1.6 or newer][go] with a [properly configured GOPATH][GOPATH].
The resulting binary does not depend on Go tools being installed, but is
platform specific. [Cross-platform building][GOOS] is easy.


[go]: https://golang.org/ "The Go Programming Language"
[GOPATH]: https://golang.org/doc/code.html#GOPATH "How to Write Go Code - The GOPATH environment variable"
[GOOS]: https://github.com/golang/go/wiki/WindowsCrossCompiling
