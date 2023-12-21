# producer.py
from kafka import KafkaProducer
import os
import time

# Kafka broker addresses from environment variable
kafka_brokers = os.environ.get("KAFKA_BROKERS", "localhost:9092")

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=kafka_brokers)

# Send messages
while True:
    producer.send("my-topic", b"Hello, Kafka!")
    print("Message sent")
    time.sleep(5)
