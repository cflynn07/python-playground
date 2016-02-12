python-api
==========

A project to aimlessly play with features of python.

Instructions
------------
Building and running code with docker, locally on OSX using docker-machine
```bash
# from python-api/ project directory
$ eval "$(docker-machine env default)" #assumes VM already set up and running
$ docker build -t 'python-api' .
$ curl http://`docker-machine ip default`:5000 -v # Hello, World!
```
