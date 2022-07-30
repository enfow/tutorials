# Celery RabbitMQ Minikube Tutorial

- Runway 에 적용하기 위한 목적으로 Celery를 Minikube에서 실행하는 Tutorial 진
- Task Producer와 Worker를 별도의 POD에 띄우는 것이 가능한지 확인하는 것을 목표로 함

## 실행 방법

### local

- run rabbitmq

```
$ docker run --network host -d --rm rabbitmq
```

- run worker

```
QUEUE=$(CELERY_QUEUE) python docker/app/app/run.py
```

- run app

```
QUEUE=$(CELERY_QUEUE) python docker/celery-worker/run.py
```


### minikube

- minikube start

```
minikube start --kubernetes-version=v1.21.13
```

- docker image build

```
eval $(minikube -p minikube docker-env) # connect minikube docker daemon and local one
docker build --tag app --file docker/app/Dockerfile .
docker build --tag celery-worker --file docker/celery-worker/Dockerfile .
```

- apply rabbitmq

```
kubectl apply -f templates/rabbitmq/deployment.yaml
kubectl apply -f templates/rabbitmq/service.yaml
```

- apply worker

```
kubectl apply -f templates/celery-worker/deployment.yaml
```

- apply app

```
kubectl apply -f templates/app/deployment.yaml
```

## 확인 사항

- Task producer 와 Worker는 동일한 task 파일을 공유해야 한다.
  - app이 다르므로 `@celery.shared_task` 를 써서 task를 정의하는 것이 좋다.
- Minikube 환경에서 Task producer와 Worker가 task queue의 이름만 공유한다면, 서로 다른 POD에서 Task를 생성/처리할 수 있다.
- Task.apply_async에서 
  - `ignore_result=False` 를 주면 결과가 돌아올 때까지 기다린다(default).
  - `ignore_result=True` 를 주면 Task 생성 후 그 결과를 기다리지 않고 넘어간다.
- 동일한 Task queue를 Consume하는 Worker를 여러 개 띄우면 하나씩 나누어 가져가 처리한다.
