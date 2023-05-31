FROM python:3.11

WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
