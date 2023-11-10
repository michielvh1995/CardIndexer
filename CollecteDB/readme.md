# CollecteDB
This is the database and Python FastAPI/Beanie API for managing the database.

The FastAPI/Beanie API can be build and run using Docker. The database itself needs to be executed from a base docker image.
Instructions for this will follow.

## Building the FastAPI/Beanie API
To build the docker container simply run `docker build -t collectedbapi .`

## Running the FastAPI/Beanie API
To run the docker container containing the API run `docker run -p 80000:3000 collectedbapi`

## Running the database
test mongoDB: `docker run -d -p 27017:27017 --name test-mongo mongo:latest`

## Debug run using uvicorn:
`uvicorn src.tmp:app --host 0.0.0.0 --port 8000`

## Running unittests
Go to `/src/` then use `python -m unittest discover -v` or `python -m unittest discover -v test`.

use `python -m unittest -v test\test_{MODULE}.py` to test individual modules (i.e. `python -m unittest -v test\test_models.py` to run the tests for the Card and CardVersion models).