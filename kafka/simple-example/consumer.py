from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "python-topic",  # topic name
    bootstrap_servers=["localhost:9092"]
)

for msg in consumer:
    print(msg.value.decode("utf-8"))  # decode bytes to string.
