# syntax=docker/dockerfile:1
FROM python:3.14-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN apt-get update && \
apt-get upgrade -y

WORKDIR /usr/src/my_service
COPY pyproject.toml .
COPY uv.lock .
RUN uv sync --frozen --no-dev --no-install-project

COPY app app/
ENV PATH="/usr/src/my_service/.venv/bin:$PATH"

RUN groupadd -g 999 apiuser && \
useradd -r -u 999 -g apiuser apiuser
USER apiuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
