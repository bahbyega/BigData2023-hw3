# Flink Window

This is a third part of the homework.
---

### Run script

```
docker compose build
docker compose up -d
docker compose ps

mkdir -p tmp/checkpoints/logs/

docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3 --partitions 3 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3-processed --partitions 3 --replication-factor 1

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/local_checkpoint.py -d

python3 part3/producer.py
python3 part3/consumer.py
```

### Example of the output
![](/part3/example.png)