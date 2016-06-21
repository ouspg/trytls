import urllib3
import sys

if len(sys.argv) < 3:
	print ("Usage: %s <hostname> <../tmp/>" % sys.argv[0])
	exit("for example: python %s localhost ../tryTLS/ssltest/services/tmp/" % sys.argv[0])	

hostname = sys.argv[1]
path = sys.argv[2]

messagefile = path + "messages"
certpath = path + "certs/"
certinfo = path + "certs/certs.info"

https = []
certnames = []

urllib3.disable_warnings()	#complains about deprecated use of CN at the moment 

with open(certinfo) as f:
	for line in f:	
		line = line.rstrip('\n')
		certnames.append(line)
		https.append(urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=('%s%s' % (certpath,line))))

ind = 0

print "\n True <-> connected, not True <-> did not connect \n\n"

with open(messagefile) as f:
	for line in f:	#port & message & certname
		port, message, certname =  line.split(' & ', 2 )		
		if certnames[ind] != certname:
			for i in range (len(certnames)):
				if certnames[i] == certname:
					ind = i
					break
		try:
			https[ind].request('GET', "https://%s:%s" % (hostname, port))	#returns message, which could be used if wanted
		except Exception as e:
			print "not True: %s" % message
		else:
			print "    True: %s" % message
