FROM python:3.9-slim as p39template

COPY ./requirements_prd.txt /tmp/requirements_prd.txt
RUN pip install --no-cache-dir -r /tmp/requirements_prd.txt

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

FROM p39template
COPY ./app /app
WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE {{cookiecutter.d4service_cache_port}}

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]
