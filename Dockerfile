FROM python:3.8.3-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc musl-dev python3-dev libffi-dev openssl-dev

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install cryptography --no-binary cryptography
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]