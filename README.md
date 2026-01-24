# Icarus

A web application written predominately in Python to track my collection of mostly old-school video games.

Icarus is distributed under the GPL V3 Licence.

## Dependencies

This software needs the following:

* Python 3
* MongoDB
* pymongo
* cherrypy
* jinja2

## Instructions

### How to run

```python Main.py```

### How to run the unit tests

```python -m unittest```

## How to make it run with Mongo

On host computer:

```
docker network create mongo-net
docker run -p 27017:27017 --network mongo-net --rm --name mongo mongodb/mongodb-community-server:latest
```

devcontainer will connect to mongo-net according to config in this repo.

There are enviornment variables, MONGO_URL and MONGO_PORT that control what gets connected to specifically. 
Using the above examples:

MONGO_URL=mongo
MONGO_PORT=27017