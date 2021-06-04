# Docker Compose Example

- Docker Compose는 여러 개의 Docker Container들을 생성하고 실행하는 것을 목적으로 사용합니다.
- 실행하고자 하는 Docker Container 각각을 Serveice라고 하며, 개별 Service의 특성은 `docker-compose.yml` 파일로 정의한다.
- [Docker Compose - Getting Started](<https://docs.docker.com/compose/gettingstarted/>)
- [Overview of docker-compose CLI](<https://docs.docker.com/compose/reference/>)
  

## docker-compose.yml

```yaml
# version of docker-compose
version: "3"
services:
  # First Service: redis-server
  redis-server:
    image: "redis"  # run with Image name

  # Second Service: node-app
  node-app:
    build: .  # build image with Dockerfile on current dir
    ports:    # port 5000 -> 8080
      - "5000:8080"
    volumes:  # Volume
      - .:/code
    environment:  # Environment variables
      ENV_V: node
```

## How to run docker-compose

### docker-compose up

- Service로 정의된 Docker Container를 생성하고 실행하는 명령어

```bash
$ docker-compose up
```

#### Options: --build

- build option을 주게 되면 Image 존재 여부와 상관없이 새롭게 Image를 Build하여 사용한다.


```bash
$ docker-compose up --build
```

### docker-compose down

- Docker compose로 실행한 Docker Container/Network/Image/Volume 등을 Stop하고 모두 삭제하는 명령어

```bash
$ docker-compose down
```

### docker-compose ps

- Docker compose로 실행한 Docker Container 들을 보여주는 명령어

```bash
$ docker-compose ps
```
