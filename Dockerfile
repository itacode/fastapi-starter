FROM python:3.9

RUN apt-get update && \
apt-get upgrade -y && \
python -m pip install --upgrade pip

WORKDIR /usr/src/my_service
COPY app app/
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry==1.4 && \
poetry export -f requirements.txt --output requirements.txt && \
pip install -r requirements.txt

RUN groupadd -g 999 apiuser && \
useradd -r -u 999 -g apiuser apiuser
USER apiuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
