# Get Started

## Usage

```bash
bash init <first-port> <hostname> <protocol> <service1> [service2] [service3 ...]
```

### Create servers on localhost

```bash
bash init 20000 localhost https initialize cert protocol cipher
```

### Build and run the servers

```bash
docker-compose build
docker-compose up
```

If no errors occured the backend should now be up and running.
 
## Other information

 * configs/* and info -file
   * init -script uses this data to generate the servers as configured.
 * tmp/* | grep "most important data" (after running the `init` -script):
   * private key (.key)
   * certificate signing request (.csr)
   * certificate (.crt)
   * server information (`server_info`)
   * server configuration (`conf`)
 * servers/*
   * docker-compose uses this data
