
##Get started

To run the stub you need to have the following installed on the testing environment:
* gcc + openssl deps

to tun the stub you need to do the following once you have java installed on your computer:
```
..# gcc -o run run.c -lssl -lcrypto
..# ./run [host] [port] [ca_bundle]
```
