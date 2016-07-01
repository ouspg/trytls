local https = require "ssl.https"

function DoThings()
  if arg[1]==nil then
    print(string.format( "Usage: %s <URL>", arg[1] ))
  else
    local r, c, h, s = https.request{
      url = tostring(arg[1]),
      sink = ltn12.sink.table({}),
      protocol = "tlsv1",
      mode = "client",
      cafile = "/etc/ssl/certs/",
      verify = "peer",
      options = "all"
    }
    print(arg[1],c)
  end
end
DoThings()
