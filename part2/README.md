# Flink Window

This is a second part of the homework.
---

### Run script

Вместо `$NAME` подставьте `session`, `sliding` или `tumbling`
```
docker compose build
docker compose up -d
docker compose ps

mkdir -p tmp/checkpoints/logs/

docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3 --partitions 3 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3-processed --partitions 3 --replication-factor 1

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/part2/$NAME.py -d

python3 producer_1.py
python3 consumer_1.py
```