# Get Started

##usage

```bash
bash init <first-port> <hostname> <protocol> <service1> [service2] [service3 ...]
```


 * to create all the services and servers(on localhost) run the following command

```bash
bash init 20000 localhost https initialize cert protocol cipher
```

 * to start the servers, you can use the docker-compose file

```bash
docker-compose build
docker-compose up
```

 * now the servers should be listening on ports `20000 ... n`
	 * `n` is the next port of the next port to ne opened if you are to start more
	 servers at the same time..ie. the ports you may want to test your code against are: `20000 ... n`

 * tmp folder content (after running the `init` -script):
	* `server key(s)` = private key
	* `server.csr` = last generated signing request, you do not need to care about this
	* `*.crt`	= cert created (and usually also used in some of your servers)
	* `server_info` = a little bit of info about servers and the messages you
	should be able to see if you were able to connect
		* ie. the configuration was supported
	* `conf` = file that includes the port(s), message(s), status(es), certificates(s) and hostname(s) used.
		* This can be created for any of the backends, not only for trytls backend 
