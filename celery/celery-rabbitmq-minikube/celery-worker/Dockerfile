FROM alpine:3.12
COPY docker/celery-worker/celery_app.py /celery-worker/celery_app.py
COPY common_task /celery-worker/common_task
RUN apk add --no-cache python3 py3-pip bash \
    && pip install 'celery~=5.2.3'

WORKDIR celery-worker
CMD ["python3", "run.py"]
# CMD python3 /celery-worker/celery_app.py \
#     --concurrency 2 \
#     --queues celery-worker \
#     --loglevel INFO

# -A 뒤에는 Celery() app 이 정의된 파일 명이 와야 함
# CMD ["celery", "-A", "celery_app", "worker", "-Q", "celery-worker", "--loglevel=INFO"]
