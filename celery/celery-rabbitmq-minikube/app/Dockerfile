FROM alpine:3.16
COPY docker/app/app ./app
COPY common_task ./app/common_task
RUN apk add --no-cache python3 py3-pip bash \
    && pip install -r app/requirements.txt
WORKDIR app
# CMD ["celery", "-A", "tasks", "worker", "--loglevel=INFO"]
CMD ["python3", "run.py"]
