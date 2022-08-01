#############################
#          Local            #
#############################
CELERY_QUEUE=celery-worker
DB_NAME=postgres

run-rabbitmq:
	docker run --network host -d --rm --name rabbitmq rabbitmq

run-postgres:
	docker run -d --network host -p 5432:5432 --name ${DB_NAME} -e POSTGRES_PASSWORD=1234 postgres

run-worker:
	QUEUE=$(CELERY_QUEUE) python celery-worker/run.py

run-app:
	QUEUE=$(CELERY_QUEUE) python app/app/run.py

attach-postgres:
	docker exec -it postgres bash -c "psql -U postgres postgres"

kill-rabbitmq:
	docker kill rabbitmq


#############################
#         Minikube          #
#############################

docker-build:
	eval $(minikube -p minikube docker-env) # connect minikube docker daemon and local one
	docker build --tag app --file app/Dockerfile .
	docker build --tag celery-worker --file celery-worker/Dockerfile .

minikube-start:
	minikube start --kubernetes-version=v1.21.13
	make docker-build

apply-rabbitmq:
	kubectl apply -f templates/rabbitmq/deployment.yaml
	kubectl apply -f templates/rabbitmq/service.yaml

apply-worker:
	kubectl apply -f templates/celery-worker/deployment.yaml

apply-app:
	kubectl apply -f templates/app/deployment.yaml

apply-celery:
	make apply-worker
	make apply-app

delete-celery:
	kubectl delete deployment/app
	kubectl delete deployment/celery-worker

reload-celery:
	make delete-celery
	make docker-build
	make apply-celery
