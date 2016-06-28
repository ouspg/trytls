local https = require "ssl.https"

function DoThings()
    if arg[1]==nil then
        print(string.format( "Usage: %s <URL>", arg[1] ))
    else
        local r, c, h, s = https.request{
            url = tostring(arg[1]),
            options = "all",
            --sink = ltn12.sink.table({}),
            protocol = "tlsv1",
            mode = "client",
            cafile = "/etc/ssl/certs/ca-certificates.crt",
            verify = "peer"
            --key = "/root/client.key",
            --certificate="/root/client.crt"
        }
        print(arg[1],c)
    end
end
DoThings()
