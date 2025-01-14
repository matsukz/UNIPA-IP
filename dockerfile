FROM python:3.11.8-slim

RUN mkdir /src
WORKDIR /src

RUN apt-get update
RUN apt-get install -y
RUN apt-get install gcc -y
RUN apt-get install default-libmysqlclient-dev -y
RUN apt-get install pkg-config -y
RUN apt-get clean

RUN pip install uvicorn fastapi