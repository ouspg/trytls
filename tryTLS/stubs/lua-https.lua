local https = require 'ssl.https'

function DoThings()
  if arg[1]==nil then
    print(string.format( "Usage: %s <URL>", arg[1] ))
    break
  else
    local r, c, h, s = https.request{
      url = tostring(arg[1]),
      sink = ltn12.sink.table({}}),
      protocol = "tlsv1"
    }
    print(r,c,h,s)
  end
end
DoThings()
