import urllib3
import sys

if len(sys.argv) < 2:
	print ("Usage: %s <../tmp/>" % sys.argv[0])
	exit("for example: python %s ../tryTLS/ssltest/services/tmp/" % sys.argv[0])	

path = sys.argv[1]

messagefile = path + "messages"
certpath = path + "certs/"
certinfo = path + "certs/certs.info"

https = []
certnames = []

with open(certinfo) as f:
	for line in f:	
		line = line.rstrip('\n')
		certnames.append(line)
		https.append(urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=('%s%s' % (certpath,line))))

ind = 0

print "\n True <-> connected, not True <-> did not connect \n\n"

with open(messagefile) as f:
	for line in f:	#port & message & certname
		port, message, certname, hostname = line.rstrip('\n').split(' & ', 4 )
		if certnames[ind] != certname:
			for i in range (len(certnames)): 
				if certname == certnames[i]:
					ind = i
					break
		try: 
			https[ind].request('GET', "https://%s:%s" % (hostname, port))	#returns message, which could be used if wanted
		except Exception as e:
			print "not True: %s" % message
		else:
			print "    True: %s" % message
