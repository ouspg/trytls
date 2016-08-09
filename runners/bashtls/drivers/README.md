# drivers

* bashTLS uses drivers to run the simplerunner.
* each one of the drivers consists of a Dockerfile and it's deps.
* when running the bashtls init-script the docker-compose is created.
*  the created docker-compose starts up the Dockerfiles when set up.
* The created image must runs at least shared/scripts/run script or a similar one to work correctly
  * have a look at the already existing Dockerfiles and you will get the idea


## In this folder you can add your own drivers
* Create folder and name it well
* Add The required files in the folder


## Example

Language: java
Driver: javac

inside the javac-folder:
 * scripts:
  * init -> install certificates  
 * Dockerfile:
  * build -> install default-jre and default-jdk 
 * driver:
  * set driver information (language ≃ command, certs = "_" -> no certs, etc)
 * loop
  * this will be invoked for all the stubs

