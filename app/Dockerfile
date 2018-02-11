FROM python:3

WORKDIR /app

RUN pip install gunicorn

COPY . /app

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "main:app"]
