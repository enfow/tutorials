# RabbitMQ Tutorial

## Installation

### Docker

- [RabbitMQ Install](<https://www.rabbitmq.com/download.html>)

```
$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
```

or

```
$ make run-rabbit
```

### Pika

- [Pika Docs](<https://pika.readthedocs.io/en/stable/>)

```
$ pip install pika
```
