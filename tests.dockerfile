FROM python:3.9

WORKDIR /home/app

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /home/app/

RUN poetry install

COPY ./src/app /home/app

ENV PYTHONPATH=/home/app

CMD ["bash", "-c", "while true; do sleep 1; done"]
