# Dockerfile in {{cookiecutter.project_slug}}/compose/local/{{cookiecutter.d4service_mq_worker_slug}}
FROM python:3.9-alpine as p39template

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "/"

COPY ./requirements_prd.txt /tmp/requirements_prd.txt
# RUN apk add --update --no-cache postgresql-client
RUN pip install --no-cache-dir -r /tmp/requirements_prd.txt

FROM p39template
COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

#RUN mkdir /Worker
#COPY ./Worker /Worker
#WORKDIR /
