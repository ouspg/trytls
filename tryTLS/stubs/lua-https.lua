local https = require "ssl.https"
local socket = require "socket"
local ssl = require "ssl"
--sink = ltn12.sink.table({}),
--key = "/root/client.key",
--certificate="/root/client.crt"
function DoThings()
    if arg[1]==nil then
        print(string.format( "Usage: %s <URL>", arg[1] ))
    else
        local r, c, h, s = https.request{
            mode = "client",
            url = tostring(arg[1]),
            protocol = "tlsv1",
            cafile = "/etc/ssl/certs/ca-certificates.crt",
            verify = "peer",
            options = "all",
        }
        print(arg[1], c, s)
    end
end
function DoOtherThings()
    local params = {
        mode = "client",
        protocol = "tlsv1",
        verify = "peer",
        options = "all",
        cafile = "/etc/ssl/certs/ca-certificates.crt"
    }

    local conn = socket.tcp()
    conn:connect(tostring(arg[1]), 443)

    conn = ssl.wrap(conn, params)
    conn:dohandshake()

    conn:send("GET / HTTP/1.1\n")
    local line, err = conn:receive("*a")
    print(arg[1], err, line)
    conn:close()
end
DoThings()
DoOtherThings()
