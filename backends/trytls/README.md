# Get Started

 * to create services and servers(on localhost) run the following command

```bash
bash init 20000 localhost https initialize cert protocol cipher
```

 * to start the servers, you can use the docker-compose file

```bash
docker-compose build
docker-compose up
```

 * now the servers should be listening on ports `100 ... n`
	 * `n` is the next port of the next port to ne opened if you are to start more
	 servers at the same time..ie. the ports you may want to test your code against are: 100 ... (n-1)

 * tmp folder content (after running the `init` -script):
	* `server key` = private key
	* `server.csr` = signing request, you do not need to care about this
	* `*.crt`	= cert created (and usually also used in some of your servers)
	* `server_info` = a little bit of info about servers and the messages you
	should be able to see if you were able to connect
		* ie. the configuration was supported
	* `messages` = "port & msg" = includes the ports listened and the corresponding
	message that should be returned if connection succeeded