# Docker Basic Commands

## docker run

```bash
$ docker run <image_name>
```

- [docker run](<https://docs.docker.com/engine/reference/run/>)
- Image에 따라 특정 프로세스를 수행하는 Container를 생성하는 명령어
- Image는 실행 명령어와 해당 명령어를 실행하는 데에 필요한 파일 스냅샷을 가지고 있다. docker run을 하게 되면 파일 스냅샷을 포함하여 Container를 구성하고, 실행 명령어를 통해 프로세스를 실행하게 된다.
 
```bash
$ docker run <image_name> <command>
```

- <image_name> 뒤에 command 를 전달하게 되면 Image의 command가 아닌 전달 받은 command를 수행하게 된다. 
- 전달하는 command는 당연히 Container 환경 내에서 실행할 수 있어야 한다.

```bash
# docker run ubuntu ls
bin
boot
dev
etc
home
lib
...
```

## docker create

```bash
$ docker create <image_name>
```

- [docker create](<https://docs.docker.com/engine/reference/commandline/create/>)
- docker run = docker create + docker start
- Image에 포함되어 있는 파일 스냅샷 등을 포함하는 Container를 생성하는 단계

## docker start

```bash
$ docker start <container ID/NAME>

# options
# -a: attach 옵션을 주어야 container의 출력 값을 확인할 수 있다(Attach STDOUT/STDERR and forward signals).
```

- [docker start](<https://docs.docker.com/engine/reference/commandline/start/>)
- docker run = docker create + docker start
- Container의 실행 명령어를 실행하는 단계

## docker exec

- [docker exec](<https://docs.docker.com/engine/reference/commandline/exec/>)
- 현재 실행 중인 Container에 실행 명령어를 전달하는 명령어

```bash
$ docker exec <container ID/NAME> <command>

# options
# -i: Interactive
# -t: Terminal
```

- `-it` 옵션을 주어 Container 내의 명령어 실행 창에 붙을 수 있다.

## docker stop & kill

- [docker stop](<https://docs.docker.com/engine/reference/commandline/stop/>)
- docker stop과 kill은 모두 현재 실행 중인 Container를 중지하는 명령어

```bash
$ docker stop <container ID/NAME>

# options
# -d: detach option을 주게 되면 background 모드로 실행된다.
```

- [docker kill](<https://docs.docker.com/engine/reference/commandline/kill/>)
- docker stop은 현재 진행 중인 작업은 마무리하고 중지
- The main process inside the container will receive SIGTERM, and after a grace period, SIGKILL.

```bash
$ docker kill <container ID/NAME>
```

- docker kill은 현재 진행 중인 작업과는 무관하게 바로 중지
- The main process inside the container is sent SIGKILL signal.

## docker rm

- [docker rm](<https://docs.docker.com/engine/reference/commandline/rm/>)
- 중지된 Container를 제거하는 명령어
- 실행 중인 Container는 제거되지 않는다.

```bash
# when trying to remove runining container
Error response from daemon: You cannot remove a running container 06310ca71c61a188d7f8a1ddd2fb10c20054d9fa8abc8850adb6ff0fb5b61389. Stop the container before attempting removal or force remove
```

```bash
$ docker rm <container ID/NAME>
```

- 모든 Container를 한 번에 지우는 명령어는 다음과 같다.

```
$ docker rm `docker ps -a -q`
```

## docker ps

```bash
$ docker ps

# options
# -a: 종료되었거나, 일시 정지 중인 Container도 포함하여 모두 보여준다.
```

- ps는 process status의 약자, 현재 실행 중인 Container를 보여주는 명령어

```bash
# kernel1: $ docker run alpine ping localhost
# kernel2: $ docker ps

CONTAINER ID   IMAGE     COMMAND            CREATED          STATUS          PORTS     NAMES
06310ca71c61   alpine    "ping localhost"   52 seconds ago   Up 51 seconds             crazy_franklin
```

- CONTAINER ID: 컨테이너 ID
- IMAGE: 컨테이너 생성에 사용된 Image
- COMMAND: 실행 명령어
- CREATED: 생성 시간
- STATUS: 현재 상태(UP: 실행 중, Exited: 종료, Pause: 일지 정지)
- PORTS: 컨테이너에서 외부에 개방하고 있는 포트
- NAMES: 컨테이너의 이름