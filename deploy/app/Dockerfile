FROM python:3.8-buster as builder

WORKDIR /opt/app/weather-api

COPY requirements.lock /opt/app/weather-api
RUN pip install -r requirements.lock

FROM python:3.8-slim-buster as runner

COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages
COPY --from=builder /usr/local/bin/flask /usr/local/bin/flask
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

COPY app /opt/app/weather-api

WORKDIR /opt/app/weather-api

CMD ["gunicorn", "app:app", "-c", "conf/gunicorn_conf.py"]
