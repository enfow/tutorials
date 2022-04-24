init:
	brew install kafka
	pip install -r requirements.txt

docker-run:
	docker compose -f docker-compose.yaml up -d

docker-down:
	docker compose down

list-topic:
	kafka-topics --bootstrap-server localhost:9092 --list

create-topic:
	kafka-topics --bootstrap-server localhost:9092 --create --topic ${TOPIC}

# e.g. $ make producer TOPIC=stream-serving-in 
producer:
	kafka-console-producer --bootstrap-server localhost:9092 --topic ${TOPIC}

# e.g. $ make consumer TOPIC=stream-serving-in 
consumer:
	kafka-console-consumer --bootstrap-server localhost:9092 --topic ${TOPIC}
