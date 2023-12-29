from kafka import KafkaConsumer


def create_consumer():
    print("Connecting to Kafka brokers")
    consumer = KafkaConsumer(
        "porsev-hw3_processed",
        group_id="hse_group",
        bootstrap_servers="localhost:29092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
    )

    for message in consumer:
        # save to DB
        print(message)


if __name__ == "__main__":
    create_consumer()
