FROM python:3.8-buster

ENV PYTHONUNBUFFERD 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
