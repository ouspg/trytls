

# Dependencies

 * This stub has been tested on OS X 10.11.5 and Python 2.7.10
 * [urllib2](https://docs.python.org/2/library/urllib2.html) is part of [python 2.7 standard library](https://docs.python.org/2/library/index.html)

# Examples

```
% python python2-urllib2/run.py sha1-2016.badssl.com 443
ACCEPT

% python python2-urllib2/run.py expired.badssl.com 443
REJECT
```

# Dealing with unexpected behavior

This stub tries to avoid a situation where traceback gets hidden on unexpected behaviour.

Manual / example test, connecting to non-existent domain:
```
% python python2-urllib2/run.py www.nosuch.example.local 443 || echo "$?"
Traceback (most recent call last):
  File "python2-urllib2/run.py", line 11, in <module>
    urllib2.urlopen("https://" + host + ":" + port, cafile=cafile)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 154, in urlopen
    return opener.open(url, data, timeout)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 431, in open
    response = self._open(req, data)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 449, in _open
    '_open', req)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 409, in _call_chain
    result = func(*args)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 1240, in https_open
    context=self._context)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/urllib2.py", line 1197, in do_open
    raise URLError(err)
urllib2.URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>

```

# Credits

Based on python3-urllib -stub.
