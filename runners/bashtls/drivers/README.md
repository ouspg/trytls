# drivers

* bashTLS uses drivers to run the simplerunner.
* each one of the drivers consists of a Dockerfile and it's deps.
* when running the bashtls init-script the docker-compose is created.
*  the created docker-compose starts up the Dockerfiles when being set up.


# In this folder you can add your own drivers
* Create folder and name it well
* Add The required files in the folder (see Driver.. below)

## Driver:
* Dockerfile and possibly other required files
* The Dockerfile builds up the image and runs at least shared/scripts/run script or a similar one
  * have a look at the already existing Dockerfiles and you will get the idea
