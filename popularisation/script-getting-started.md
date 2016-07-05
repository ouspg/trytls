Hi!

I'm FixMe and I'm here to tell you how to contribute to TryTLS.
It's pretty simple: you just need, X, Y, and Z and you are ready
to follow my instructions.

You can run TryTLS on your on computer, or in the cloud. From cloud
services we like to use X, Y, and Z, as they play along nicely with Docker.

# Decide: docker or native

First thing you need to do is to decide if you want to use Docker, or
run TryTLS natively. With Docker you keep your main
computing environment free from clutter. However, if you already have the target
you want to test installed, you do not necessarily need to use it.

## Native

### Test one stub

First thing we recommend you to do is to test one of the existing stubs.
Directory ```stubs/```, shows us all the stubs that community has done already
<show the stubs-directory with browser>.

I think I'm goint to use python-urllib2 as both python 2.7 and urllib2 are
installed in my environment.

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
information soon. You can see the install path from this line.

<highlight the following line with mouse?>

```
Installing trytls script to /Users/user/Library/Python/2.7/bin
```

It is time to have a go.

First, I'll use the trytls runner to run a bundle of tests.

```
$ cd stubs
$ /Users/user/Library/Python/2.7/bin/trytls -t
```

Next, I'll pick the bundle. I'm going to test https-connectivity, so
I'm picking https-bundle with the -t.

<FixMe> are the bundles already in official documentation? If they are,
show them in video?

Continue:

```
$ /Users/user/Library/Python/2.7/bin/trytls -t .https.all_tests
```

Finally, pick the command and stub which will execute the tests, as instructed
by trytls.


```
$ /Users/user/Library/Python/2.7/bin/trytls -t .https.all_tests python python-urllib2/run.py
```

There you go! Now you have experience from running a working stub and you are
prepared to write your own stub!

### Write your own stub

<steps>

## Docker

### Test one dockerfile

<steps>

### Create an environment for your stub

<steps>

### Set up our Docker-based backend

<steps>
