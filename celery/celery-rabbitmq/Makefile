run-celery:
	celery -A tasks worker --loglevel=INFO

run-rabbitmq:
	docker run -d --rm --name rabbitmq -p 5672:5672 rabbitmq
