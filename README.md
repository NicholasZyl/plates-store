# License plates store

## Development
This project uses [poetry](https://python-poetry.org/) for managing dependencies. After fetching the code please run
the following to get all dependencies:
```commandline
poetry install
```
To ensure the same styleguide used in the project, safety of the dependencies and working code, this project uses
[pre-commit](https://pre-commit.com/) package which runs checks before each commit. When you set up the project for
the first time please run:
```commandline
poetry run pre-commit install
```
### Local environment
Local environment is built with docker. It consists of a dedicated API container based on the
[Python base image](https://hub.docker.com/_/python) ([Dockerfile](./Dockerfile)) and
[PostgreSQL](https://hub.docker.com/_/postgres). To run the environment start it with the docker-compose command
```commandline
docker-compose up
```
If you run it for the first time, you have to set up the database schema. You can do it with
a dedicated command:
```commandline
docker-compose exec api flask init init-db
```
To run tests you can run:
```commandline
# to run the whole test suite
poetry run pytest src tests

# to run e2e tests
poetry run pytest src tests/e2e

# to run integration tests
poetry run pytest src tests/integration

# to run unit tests
poetry run pytest src tests/unit
```
