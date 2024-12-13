FROM ubuntu:24.04

RUN apt-get update
RUN apt-get install -y \
    python3 \
    python3-flask \
    gunicorn

ADD . /app
WORKDIR /app

CMD ["/usr/bin/gunicorn", "--bind", "0.0.0.0:8080", "--threads", "16",  "--access-logfile", "-", "app:app"]

