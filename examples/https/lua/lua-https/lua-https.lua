local https = require "ssl.https"
local socket = require "socket"
local ssl = require "ssl"

function tablelength(T)
    local count = 0
    for _ in pairs(T) do count = count + 1 end
    return count
end

function DoOtherThings()
    if tablelength(arg)<4 then
        print(string.format( "Usage: %s <URL> <PORT> (<CA-BUNDLE>)", arg[0] ))
    else
        local params = {
            mode = "client",
            protocol = "tlsv1",
            verify = "peer",
            options = "all",
            cafile = "/etc/ssl/certs/ca-certificates.crt" or arg[3],
        }

        local conn = socket.tcp()
        conn:connect(tostring(arg[1]), arg[2])

        conn = ssl.wrap(conn, params)
        conn:dohandshake()

        conn:send("GET / HTTP/1.1\n\n")
        local line, err = conn:receive()
        print(arg[1], err, line)
        conn:close()
    end
end

DoOtherThings()
