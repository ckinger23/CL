FROM python:3.7.5-slim-buster
MAINTAINER Nick Williams <wilnq20@gmail.com>

RUN apt-get update && apt-get install -qq -y \
	build-essential libpq-dev --no-install-recommends

ENV INSTALL_PATH /coinlogic
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .


CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "coinlogic.app:create_app()"
