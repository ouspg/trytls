# Testing trytls with an existing stub.

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

## Install trytls

Then I'm going to install trytls libs.

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
information soon. You can see the install path from the "Installing trytls script..."
-line.

## Give it a go.

It is time to have a go.

First, I'll use the trytls runner to run a bundle of tests.
(Remember to replace the example path to the one that matches your setup!)

```
$ cd stubs
$ /Users/user/Library/Python/2.7/bin/trytls -t
```

Next, I will select the bundle. I'm going to test https-connectivity, so
I'm picking https-bundle with the -t. The available bundles are listed in
[showrunner's README.md](https://github.com/ouspg/trytls/blob/master/showrunner/README.md#built-in-bundles)

```
$ /Users/user/Library/Python/2.7/bin/trytls -t .https.all_tests
```

Finally, pick the command and stub which will execute the tests, as instructed
by trytls. I'm testing python's urllib2, so my command is ```python``` and my stub is ```python-urllib2/run.py```

```
$ /Users/user/Library/Python/2.7/bin/trytls -t .https.all_tests python python-urllib2/run.py
PASS badssl(False, 'expired')
PASS badssl(False, 'wrong.host')
PASS badssl(False, 'self-signed')
...
```

There you go! Now you have experience from running a working stub and you are
prepared to write your own stub!
