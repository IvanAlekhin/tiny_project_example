FROM python:3.8-slim
WORKDIR /app
RUN pip3 install pipenv
COPY Pipfile* ./
RUN pipenv install --dev --system --deploy

COPY src src
COPY main.py main.py
COPY tests tests