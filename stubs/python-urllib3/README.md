
# How to run:

```
python run.py <url> <port> [ca_file]
```

For example:

```
$ python stubs/python-urllib3/run.py sha256.badssl.com 443
VERIFY REJECT
```

# Dependencies:

Python
urllib3 installed (`pip install urllib3` to command line)
certifi installed (`pip install certifi` to command line)

Tested on Ubuntu 16.04
