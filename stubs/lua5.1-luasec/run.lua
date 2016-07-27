local socket = require "socket"
local ssl = require "ssl"
--local apr = require "apr"

function tablelength(T)
    local count = 0
    for _ in pairs(T) do count = count + 1 end
    return count
end

function main()
    if tablelength(arg)==5 then
        cert = arg[3]

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
            print("ACCEPT")
        else
            print(err)
            print("REJECT")
        end
        conn:close()
    elseif tablelength(arg) == 4 then
        print("UNSUPPORTED")
    else
        print(string.format( "Usage: %s <HOST> <PORT> (<CA-BUNDLE>)", arg[0] ))
        os.exit(1)
    end
end

main()
