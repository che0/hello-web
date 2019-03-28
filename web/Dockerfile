FROM python:3
MAINTAINER Petr Novák 2 <petr.novak2@firma.seznam.cz>

RUN pip install uwsgi flask requests jinja2
COPY . /app

ADD https://github.com/che0/uwping/releases/download/14.0/uwping /usr/local/bin/uwping
RUN chmod +x /usr/local/bin/uwping

WORKDIR /app

EXPOSE 9090
CMD ["uwsgi", \
        "--socket=:9090", "--processes=4", \
        "--uid=nobody", "--gid=nogroup", \
        "--need-app", \
        "--module=hello:app"]
