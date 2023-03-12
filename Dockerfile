FROM python:3.11.1-alpine

WORKDIR /dppr
COPY . .
RUN pip install poetry==1.3.2
RUN poetry install; exit 0

ENTRYPOINT poetry run python main.py