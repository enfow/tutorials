# Kafka tutorial

## Install and run kafka

### local

- mac에서는 brew로 쉽게 설치가 가능하다.

```
$ brew install kafka
```

### docker

- `bitnami` docker image를 사용하여 kafka와 zookeeper 를 띄울 수 있다.
- [Kafka docker image by bitnami](<https://hub.docker.com/r/bitnami/kafka>)

```yaml
# docker/docker-compose.yaml
# https://github.com/bitnami/bitnami-docker-kafka
version: "3"
services:
  zookeeper:
    image: 'bitnami/zookeeper:latest'
    ports:
      - '2181:2181'
    environment:
      - ALLOW_ANONYMOUS_LOGIN=yes
  kafka:
    image: 'bitnami/kafka:latest'
    ports:
      - '9092:9092'
    environment:
      - KAFKA_BROKER_ID=1
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://127.0.0.1:9092
      - KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181
      - ALLOW_PLAINTEXT_LISTENER=yes
    depends_on:
      - zookeeper
```

## Commands

### kafka-topics

```bash
# get kafka topics
$ kafka-topics --bootstrap-server localhost:9092 --list

# create new kafka topics
$ kafka-topics --bootstrap-server localhost:9092 --create --topic [TOPIC NAME]

# create new kafka topics (with more options)
$ kafka-topics \
    --bootstrap-server localhost:9092 \
    --create \
    --topic [TOPIC NAME] \
    --partitions [N PARTITIONS] \
    --replication-factor [N REPLICA] \  # should bigger than N Brokers

# describe topics
$ kafka-topics --bootstrap-server localhost:9092 --describe

# delete topics
$ kafka-topics --bootstrap-server localhost:9092 --delete --topic [TOPIC NAME]
```

#### example

```
$ kafka-topics --bootstrap-server localhost:9092 --create --topic first-topic --partitions 3
Created topic first-topic.

$ kafka-topics --bootstrap-server localhost:9092 --describe
Topic: first-topic      TopicId: e4vD-ewqRw6CcaorXLhuig PartitionCount: 3       ReplicationFactor: 1    Configs: segment.bytes=1073741824
        Topic: first-topic      Partition: 0    Leader: 1       Replicas: 1     Isr: 1
        Topic: first-topic      Partition: 1    Leader: 1       Replicas: 1     Isr: 1
        Topic: first-topic      Partition: 2    Leader: 1       Replicas: 1     Isr: 1
```

### kafka-console-producer and kafka-console-consumer

```
# producing topic
$ kafka-console-producer --bootstrap-server localhost:9092 --topic [TOPIC NAME]

# producing topic
$ kafka-console-producer \
    --bootstrap-server localhost:9092 \
    --topic [TOPIC NAME] \
    --property parse.key=true \  # pass data as key:value
    --property key.separator=:   # the separator is `:`
```

```
# consuming topic
$ kafka-console-producer --bootstrap-server localhost:9092 --topic [TOPIC NAME]

# consuming topic
$ kafka-console-producer \
	--bootstrap-server localhost:9092 \
	--topic [TOPIC NAME] \
	--property print.timestamp=true \
	--property print.key=true \ 
	--property print.value=true \
	--from-beginning \ 			# print all of the msg from the beginning.
	--group [GROUP NAME]
```

#### example

```
$ kafka-console-producer --bootstrap-server localhost:9092 --topic first-topic
>I love kafka

===============================================================================
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic first-topic
I love kafka

```

- 존재하지 않는 topic으로 producing/consuming 하면 해당 이름을 가진 새로운 Topic을 생성한다: Auto Creation mechanism

```
# second-topic does not exist.
$ kafka-console-producer --bootstrap-server localhost:9092 --topic second-topic  
>It is Second
[2022-03-20 22:09:25,074] WARN [Producer clientId=console-producer] Error while fetching metadata with correlation id 3 : {second-topic=LEADER_NOT_AVAILABLE} (org.apache.kafka.clients.NetworkClient)
>It is Second

===============================================================================
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic second-topic
It is Second
 ```

- key:value 구조로 producing 할 수 있다.
  - 이때 key:value 구조가 아닌 값이 들어오면 producer는 죽는다.
  - consumer에는 value만 들어온다. 

```
$ kafka-console-producer --bootstrap-server localhost:9092 --topic fourth-topic --property parse.key=true --prope
rty key.separator=:
>a:b		# key:value
>a			# non key:value
org.apache.kafka.common.KafkaException: No key found on line 2: a
        at kafka.tools.ConsoleProducer$LineMessageReader.readMessage(ConsoleProducer.scala:292)
        at kafka.tools.ConsoleProducer$.main(ConsoleProducer.scala:51)
        at kafka.tools.ConsoleProducer.main(ConsoleProducer.scala)

===============================================================================
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic fourth-topic
b
```

- `--property` 를 통해 key:value와 timestamp도 같이 표시할 수 있다.

```
kafka-console-producer --bootstrap-server localhost:9092 --topic fourth-topic --property parse.key=true --property key.separator=:
>a:b
>a:c
>a:d

kafka-console-consumer --bootstrap-server localhost:9092 --topic fourth-topic --property print.timestamp=true --property print.key=true --property print.value=true
CreateTime:1647782329147        a       b
CreateTime:1647782347919        a       c
CreateTime:1647783303931        a       d
```

- group 을 사용하면 consumer들이 topic에서 partition별로 서로 나누어 message를 가져간다.
- Group 설정이 없는 경우 -> 각 consumer가 producing된 message를 모두 출력함 

```
[without group]
==PRODUCER=====================================================================
$ kafka-console-producer --bootstrap-server localhost:9092 --topic first-topic --property parse.key=true --property key.separator=:
>without:group

==CONSUMER1====================================================================
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic first-topic --property print.key=true --property print.value=true
without group

==CONSUMER2====================================================================
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic first-topic --property print.key=true --property print.value=true
without group

==CONSUMER2====================================================================
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic first-topic --property print.key=true --property print.value=true
without group
```

- Group 설정이 있는 경우 -> producing된 message를 comsumer가 서로 나누어서 출력함

```
[with group]

==PRODUCER=====================================================================
$ kafka-console-producer --bootstrap-server localhost:9092 --topic first-topic --property parse.key=true --property key.separator=:
>first:msg
>second:msg
>third:msg
>fourth:msg
>fifth:msg
>sixth:msg
>seventh:msg
>eighth:msg

==CONSUMER1====================================================================
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic first-topic --property print.key=true --property print.value=true --group first-group

first   msg
second  msg

==CONSUMER2====================================================================
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic first-topic --property print.key=true --property print.value=true --group first-group

third   msg
fourth  msg
fifth   msg
sixth   msg
eighth  msg

==CONSUMER2====================================================================
$ kafka-console-consumer --bootstrap-server localhost:9092 --topic first-topic --property print.key=true --property print.value=true --group first-group
kafka-console-consumer --bootstrap-server localhost:9092 --topic first-topic --property print.key=true --property print.value=true --group first-group

seventh msg
```
