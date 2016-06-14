# TryTLS

## Why?
* Potentially overlooked issue: many popular libraries may have broken certificate checks -> large vulnerability

## Who?
* Mauri Miettinen
* Aleksi Klasila

## To whom?
* Software and library developers
* People who write checks and want to contribute

## What
* Check the language behaviour of a software library - does it properly check the certificates?

## How
* Open public project created with scalability in mind, with ease of access provided by per-case documentation
* Utilize Docker to create a virtual environment -> anyone can contribute
* "Checking of checks" -> how libraries handle signatures, domain names, time, SNI etc.
* Ease of testing via options -> Run own server on the host or run the same container in the cloud
* Provide both end results and the source material used to get those results, enabling reproduction
* Use ports and virtual hosts to provide falsified/broken certificate checks

