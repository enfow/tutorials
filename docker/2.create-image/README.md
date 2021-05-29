# Create Docker Image

- Docker Image는 Container를 만드는 데에 필요한 명령어, 설정 값, 정보 등을 포함하고 있는 데이터 덩어리이다.
- Docker Image 생성 단계는 다음과 같다.

## 1. Dockerfile

- [Best practices for writing Dockerfiles](<https://docs.docker.com/develop/develop-images/dockerfile_best-practices/>)
- 특정 Docker Image를 생성하는 데에 필요한 명령어들이 저장되어 있는 파일

```bash
# example of Dockerfile
# syntax=docker/dockerfile:1
FROM ubuntu:18.04
COPY . /app
RUN make /app
CMD python /app/app.py
```

- FROM: Base image(OS) 설정
- COPY: 추가할 파일 명시
- RUN: build시 수행할 명령어
- CMD: Container 실행 시 수행할 명령어

## 2. docker build

- [docker build](<https://docs.docker.com/engine/reference/commandline/build/>)
- docker build 명령어를 Dockerfile이 존재하는 디렉토리를 전달하여 실행한다.
- 생성하고자 하는 docker image의 이름은 `-t` option으로 전달할 수 있다.

```bash
# in `create-image/` directory
$ docker build ./

# option
#-t: 생성하려는 docker image 이름을 설정할 때 사용된다.
```

- 참고로 `create-image` 디렉토리의 Dockerfile 내용은 아래와 같다.
  - ubuntu:20.04를 운영체제로 한다.
  - ./example directory의 파일들을 /example/ directory에 저장한다.
  - python을 설치한다.
  - `python3 /example/hello_world.py` 을 실행한다.

```bash
# create-image/Dockerfile
FROM ubuntu:20.04 

COPY ./example/* /example/

RUN apt-get update && \
    apt-get install -y python3.8 && \
    apt-get install -y python3-pip && \
    pip install -r /example/requirements.txt

CMD ["python3", "/example/hello_world.py"]
```

apt-get install 과 같이 `[Y/n]`을 입력해주어야 하는 경우 `-y` 옵션을 추가해주어야 한다. 그렇지 않은 경우 다음과 같은 Error가 발생한다.

```bash
#7 17.72 Do you want to continue? [Y/n] Abort.
------
executor failed running [/bin/sh -c apt-get update && apt-get install -y python3.8 && apt-get install python3-pip]: exit code: 1
```

## 3. Check Created image

- Image list에 `enfow/hello`로 새로운 image 생성 확인

```bash
# $ docker images
REPOSITORY                           TAG       IMAGE ID       CREATED         SIZE
enfow/hello                          latest    f9be72b8badc   4 minutes ago   470MB
```

- docker run 실행 시 `Hello World` 출력 확인

```bash
# $ docker run enfow/hello
Hello World
```