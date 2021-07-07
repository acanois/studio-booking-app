# syntax=docker/dockerfile:1
FROM nikolaik/python-nodejs:latest
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY package.json /code/
RUN yarn install
COPY . /code/