local socket = require "socket"
local ssl = require "ssl"
--local apr = require "apr"

function tablelength(T)
    local count = 0
    for _ in pairs(T) do count = count + 1 end
    return count
end

function main()
    if tablelength(arg)<4 or tablelength(arg)>5 then
        print(string.format( "Usage: %s <URL> <PORT> (<CA-BUNDLE>)", arg[0] ))
    else
        local cert = "/etc/ssl/certs/ca-certificates.crt"
        if arg[3] then
            cert = arg[3]
        end

        local params = {
            mode = "client",
            protocol = "any",
            verify = "peer",
            options = "all",
            cafile = cert
        }

        local conn = socket.tcp()
        conn:connect(arg[1], arg[2])

        conn = ssl.wrap(conn, params)
        conn:sni(arg[1])
        local succ,err = conn:dohandshake()

        if succ then
            print("VERIFY SUCCESS")
        else
            print(err)
            print("VERIFY FAILURE")
        end
        conn:close()
    end
end

main()
