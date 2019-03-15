FROM python:3
MAINTAINER Petr Novák 2 <petr.novak2@firma.seznam.cz>

RUN pip install flask requests jinja2
COPY app /app
WORKDIR /app

EXPOSE 80
CMD ["python3", "/app/hello.py"]
