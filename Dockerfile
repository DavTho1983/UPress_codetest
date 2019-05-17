FROM python:3.7-alpine
MAINTAINER Freshness Productions

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /UPress_codetest
WORKDIR /UPress_codetest
COPY ./UPress_codetest /UPress_codetest

RUN adduser -D user
USER user