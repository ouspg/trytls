local socket = require "socket"
local ssl = require "ssl"
--local apr = require "apr"

function tablelength(T)
    local count = 0
    for _ in pairs(T) do count = count + 1 end
    return count
end

------ From https://github.com/bartbes/luasec/blob/cde151739e4f7d9262dcea462a2e58d708501ad8/src/ssl.lua
local function checkhostname_single(hostname, cn)
    if cn:match("^%*%.") then
        hostname = hostname:match("%.(.+)$")
        cn = cn:match("%.(.+)$")
        if cn == "" or hostname == "" then return false end
    end
    return cn == hostname
end
local function checkhostname(cert, hostname)
  local subject, ext
  subject = cert:subject()
  for i, v in ipairs(subject) do
    if v.name == "commonName" then
      if checkhostname_single(hostname, v.value) then
        return true
      end
      break
    end
  end
  -- If we got here, the cn doesn't match, check for the dNSName extension
  ext = (cert:extensions() or {})["2.5.29.17"]
  if not ext or not ext.dNSName then return false end
  for i, v in ipairs(ext.dNSName) do
    if checkhostname_single(hostname, v) then
      return true
    end
  end
  return false
end
-----------------

function main()
    if tablelength(arg)<4 then
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
            local cert = conn:getpeercertificate()
            if checkhostname(cert, arg[1]) then
                print("VERIFY SUCCESS")
            else
                print("VERIFY FAILURE")
            end
        else
            print("VERIFY FAILURE")
        end
        conn:close()
    end
end

main()
