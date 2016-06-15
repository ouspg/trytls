# Get started
To run for example the https localhost servers:
  * go to the folder https/localhost/
  * build the docker-compose: docker-compose build
  * run it: docker-compose run


# Ports
  * port: 100: valid cert
  * port: 101: wrond hostname

#Test Your Setup

You can test that the set up is correct for example with some of the following tests_

```
curl https://localhost:100     -> ok(valid cert) - connected
curl https://localhost:101     -> hostname doesn't match target host name 'local host'
curl https://localhost:101 -k  -> fail(hostname): hostname did not match target host name - connected, ignores the problems == doesn't check
```
