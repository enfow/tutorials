init:
	brew install kafka
	pip install -r requirements.txt

docker-run:
	docker compose -f docker-compose.yaml up -d

docker-down:
	docker compose down

topic-list:
	kafka-topics --bootstrap-server localhost:9092 --list

producer:
	kafka-console-producer --bootstrap-server localhost:9092 --topic ${TOPIC}

consumer:
	kafka-console-consumer --bootstrap-server localhost:9092 --topic ${TOPIC}
