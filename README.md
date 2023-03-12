# FastAPI starter
A boilerplate to start developing microservices in Python.

## Features
- Web framework [FastAPI](https://fastapi.tiangolo.com/)
- Production ASGI web server [Uvicorn](https://www.uvicorn.org/)
- Interactive API [documentation](http://localhost:8000/docs)
- Environment variables file `.env` for the app configuration
- Docker `docker-compose.yml` and `Dockerfile` to run the prodution server
- Openapi generator [openapi-generator-cli](https://github.com/OpenAPITools/openapi-generator-cli) configured to generate clients
- MySQL database with docker compose
- ORM [SQLAlchemy](https://www.sqlalchemy.org/)
- Data validator [Pydantic](https://pydantic-docs.helpmanual.io/)
- Unit test framework [pytest](https://docs.pytest.org/en/7.1.x/contents.html)
- Linter [Flake8](https://flake8.pycqa.org/en/latest/)
- Code formatter [Black](https://black.readthedocs.io/en/stable/)
- Imports sorter [isort](https://pycqa.github.io/isort/)
- Static type checker [Mypy](http://mypy-lang.org/)

## Installation
Visual Studio Code is the recommended editor, please install the recommended extensions in `.vscode/extensions.json`.

Install [poetry](https://python-poetry.org/docs/#installation).

Install dependencies:
```shell
poetry install
```

## Development
Start the development server with automatic reload:
```shell
poetry shell
dev
```
or
```shell
uvicorn app.main:app --reload
```

### Run database Docker
Run:
```shell
cd db
docker compose up -d --build
```
Stop:
```shell
cd db
docker compose down
```

### Unit test
```shell
poetry shell
pytest
```

### OpenAPI generator
In `openapi-generator` install the required packages:
```shell
npm install
```
Start the server then generate clients:
```shell
npm run generate
```

## Server Docker
In the project root there is the `docker-compose.yml`.

Run:
```shell
docker compose up -d --build
```
Stop:
```shell
docker compose down
```

## Production server
```shell
poetry shell
uvicorn app.main:app
```
