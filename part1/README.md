# Local setup of `flink`+`kafka`

This is a first part of the homework. Done by Denis Porsev.
---


### Docker-compose configuration

```
docker compose build
docker compose up -d
docker compose ps
```
![](/part1/build.png)
![](/part1/up.png)
![](/part1/ps.png)


### Log collection configuration
```
mkdir -p tmp/checkpoints/logs/
```

### Kafka topics
```
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3 --partitions 3 --replication-factor 1

docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3-processed --partitions 3 --replication-factor 1
```

### Run
```
docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/local_checkpoint.py -d
```

![](/part1/logs.png)
![](/part1/runningJob1.png)
![](/part1/runningJob2.png)


### Whole script
```
docker compose build
docker compose up -d
docker compose ps

mkdir -p tmp/checkpoints/logs/

docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3 --partitions 3 --replication-factor 1
docker-compose exec kafka kafka-topics.sh --bootstrap-server kafka:9092 --create --topic hw3-processed --partitions 3 --replication-factor 1

docker-compose exec jobmanager ./bin/flink run -py /opt/pyflink/local_checkpoint.py -d

python3 producer_1.py
python3 consumer_1.py
```

![](/part1/producer.png)