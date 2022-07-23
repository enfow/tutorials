minikube-start:
	minikube start --kubernetes-version=v1.21.13
	eval $(minikube -p minikube docker-env)  # register local docker registry

apply-rabbitmq:
	kubectl apply -f templates/rabbitmq/deployment.yaml
	kubectl apply -f templates/rabbitmq/service.yaml

apply-celery-worker:
	kubectl apply -f templates/celery-worker/deployment.yaml
