"""Define kafka producer with console input.

author: kyeongmin woo
email: wgm0601@gmail.com
"""

import argparse
from kafka import KafkaProducer
import time

def run(bootstrap_server: str, topic: str):
    producer = KafkaProducer(bootstrap_servers=[bootstrap_server], acks="all")

    if not producer.bootstrap_connected():
        print("connection failed.")
        exit()

    while True:
        # why encoding: availiable msg types: bytes, bytearray, memoryview, type(None)
        msg = input().encode("utf-8")
        # send message
        producer.send(
            topic=topic,
            value=msg,  
        )
        # why flush(): https://stackoverflow.com/questions/45092857/kafka-produce-send-never-sends-the-message
        producer.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--bootstrap-server', type=str, default="localhost:9092")
    parser.add_argument('--topic', type=str, default="python-topic")

    args = parser.parse_args()
    run(bootstrap_server=args.bootstrap_server, topic=args.topic)
