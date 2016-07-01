local https = require "ssl.https"
local socket = require "socket"
local ssl = require "ssl"

function tablelength(T)
    local count = 0
    for _ in pairs(T) do count = count + 1 end
    return count
end
function DoThings()
    if tablelength(arg)<4 then
        print(string.format( "Usage: %s <URL> <PORT> (<CA-BUNDLE>)", arg[0] ))
    else
        local cert = "/etc/ssl/certs/ca-certificates.crt"
        if not arg[3]==nil then
            cert = arg[3]
        end
        print(cert)
        local body, code, headers, status = https.request({
            url = arg[1],
            mode = "client",
            protocol = "tlsv1",
            verify = "peer",
            options = "all",
            cafile = cert,
        })
        print(body,code,headers,status)
    end
end
function DoOtherThings()
    if tablelength(arg)<4 then
        print(string.format( "Usage: %s <URL> <PORT> (<CA-BUNDLE>)", arg[0] ))
    else
        local cert = "/etc/ssl/certs/ca-certificates.crt"
        if not arg[3]==nil then
            cert = arg[3]
        end
        print(arg[1], arg[2], arg[3])
        print(cert)
        local params = {
            mode = "client",
            protocol = "tlsv1",
            verify = "peer",
            options = "all",
            cafile = cert,
        }

        local conn = socket.tcp()
        conn=net.createConnection(net.TCP, false)
        conn:connect(tostring(arg[1]), arg[2])

        conn = ssl.wrap(conn, params)
        conn:dohandshake()

        conn:send("GET / HTTP/1.1\n\n")
        local line, err = conn:receive()
        print(err or line)
        conn:close()
    end
end

DoOtherThings()
--DoThings()
