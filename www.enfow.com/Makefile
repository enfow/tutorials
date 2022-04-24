DEV_IMAGE = enfow.docker:dev
PROD_IMAGE = enfow.docker:prod

docker-build-dev:
	docker build -t ${DEV_IMAGE} .

docker-run-dev:
	docker run --rm -d -p 5005:3000 ${DEV_IMAGE}

docker-build:
	docker build -t ${PROD_IMAGE} -f Dockerfile.prod .

docker-run:
	docker run --rm -d -p 5005:3000 ${PROD_IMAGE}
