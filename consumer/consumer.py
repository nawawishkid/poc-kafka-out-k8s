from kafka import KafkaConsumer
import os

kafka_brokers = os.environ.get("KAFKA_BROKERS", "localhost:9092")

consumer = KafkaConsumer(
    "my-topic",
    bootstrap_servers=kafka_brokers,
    group_id="my-group",
    auto_offset_reset="earliest",
)

for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
