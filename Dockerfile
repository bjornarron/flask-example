FROM alpine:3.14

RUN apk update && \
    apk add --no-cache git \
        build-base \
        libffi-dev \
        openssl-dev \
        python3-dev \
        py3-pip \
        postgresql-dev \
        gcc \
        musl-dev


WORKDIR /app

RUN git clone https://github.com/bjornarron/flask-example.git
RUN pip3 install psycopg2-binary

WORKDIR /app/flask-example

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]
