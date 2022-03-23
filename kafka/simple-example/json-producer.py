"""Define kafka producer with json serializer.

author: kyeongmin woo
email: wgm0601@gmail.com
"""
import torch
import numpy as np
import pandas as pd
import argparse
from kafka import KafkaProducer
import time
import json
import pickle

def run(bootstrap_server: str, topic: str):
    producer = KafkaProducer(
        bootstrap_servers=[bootstrap_server],
        # value_serializer=lambda v: json.dumps(v).encode('utf-8'),  # json serializer
        value_serializer=lambda v: pickle.dumps(v),
        acks="all"
    )

    if not producer.bootstrap_connected():
        print("connection failed.")
        exit()

    msg = {
        "list" : [1,2,3],
        "dict" : {"first" : 1, "second" : 2}
    }
    producer.send(
        topic=topic,
        value=msg,  
    )
    producer.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--bootstrap-server', type=str, default="localhost:9092")
    parser.add_argument('--topic', type=str, default="python-topic")

    args = parser.parse_args()
    run(bootstrap_server=args.bootstrap_server, topic=args.topic)
