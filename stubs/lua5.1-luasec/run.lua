local socket = require "socket"
local ssl = require "ssl"

function tablelength(T)
    local count = 0
    for _ in pairs(T) do count = count + 1 end
    return count
end

function main()
    if tablelength(arg)<4 then
        print(string.format( "Usage: %s <URL> <PORT> (<CA-BUNDLE>)", arg[0] ))
    else
        local cert = "/etc/ssl/certs/ca-certificates.crt"
        if not arg[3]==nil then
            cert = arg[3]
        end

        local params = {
            mode = "client",
            protocol = "any",
            verify = "peer",
            options = "all",
            cafile = cert,
        }

        local conn = socket.tcp()
        conn:connect(arg[1], arg[2])

        conn = ssl.wrap(conn, params)
        conn:sni(arg[1])
        local err = conn:dohandshake()
        conn:close()

        if err then
            print("VERIFY SUCCESS")
        else
            print("VERIFY FAILURE")
        end
    end
end

main()
