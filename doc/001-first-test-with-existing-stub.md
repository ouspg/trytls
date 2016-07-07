# Testing TryTLS with an existing stub.

First thing we recommend you to do is to test one of the existing stubs.
Directory ```stubs/```, shows us all the stubs that community has done already
<show the stubs-directory with browser>.

I think I'm going to use python-urllib2 as both python 2.7 and urllib2 are
installed in my environment.

## Get the source

First thing to do is to clone the repository.

```
$ git clone https://github.com/ouspg/trytls.git
Cloning into 'trytls'...
remote: Counting objects: 1249, done.
remote: Compressing objects: 100% (57/57), done.
remote: Total 1249 (delta 21), reused 0 (delta 0), pack-reused 1186
Receiving objects: 100% (1249/1249), 4.60 MiB | 2.47 MiB/s, done.
Resolving deltas: 100% (482/482), done.
Checking connectivity... done.
```

## Install TryTLS


```
$ cd trytls
$ python setup.py install --user
running install
running bdist_egg
running egg_info
creating trytls.egg-info
writing trytls.egg-info/PKG-INFO
....
Installing trytls script to /Users/user/Library/Python/2.7/bin
```

Now, pay attention to where the trytls script was installed. You will need that
information soon. You can see the install path from the ```Installing trytls script```...
-line.

## Give it a go.

It is time to have a go.

First, I'll use the trytls runner to run a bundle of tests.
(Remember to replace the example path to the one that matches your setup!)

```
$ cd stubs
$ /Users/user/Library/Python/2.7/bin/trytls
usage: trytls BUNDLE COMMAND [ARG ...]
trytls: error: missing the bundle argument

Valid bundle options:
  handshake
  https
  imap

```

Next, select the test bundle you wish to run. I'm going to test https-connectivity, so I'll instruct trytls to use https-bundle.

```
$ /Users/user/Library/Python/2.7/bin/trytls https
```

Finally, pick the command and stub for executing the tests, as instructed by trytls. I'm testing python's urllib2, so my command is ```python``` and my stub is ```python-urllib2/run.py```

```
$ /Users/user/Library/Python/2.7/bin/trytls https python python-urllib2/run.py
PASS badssl(False, 'expired')
PASS badssl(False, 'wrong.host')
PASS badssl(False, 'self-signed')
...
```

There you go! Now you have experience from running a working stub and you are prepared to write your own stub!
