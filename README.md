# License plates store

## Development
This project uses [poetry](https://python-poetry.org/) for managing dependencies. After fetching the code please run
the following to get all dependencies:
```commandline
poetry install
```
To ensure the same styleguide used in the project, safety of the dependencies and working code, this project uses
[pre-commit](https://pre-commit.com/) package which runs checks before each commit. When you setup the project for
the first time please run:
```commandline
poetry run pre-commit install
```
