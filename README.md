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
- Linter and code formatter [Ruff](https://docs.astral.sh/ruff/)

## Installation

Visual Studio Code is the recommended editor, please install the recommended extensions in `.vscode/extensions.json`.

Install [uv](https://docs.astral.sh/uv/getting-started/installation/).

Install dependencies

```shell
uv sync
```

## Development

Run the development server with automatic restart

```shell
uv run dev
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
pytest
```

### OpenAPI generator

In `openapi-generator` install the required packages

```shell
npm install
```

Start the server then generate clients

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
uvicorn app.main:app
```
