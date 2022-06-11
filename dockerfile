FROM python:3.8-slim-buster

WORKDIR /usr/src/app

RUN apt-get update && apt install -y netcat

COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

RUN mkdir /usr/src/media

COPY . .



