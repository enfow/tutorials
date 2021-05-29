# Docker Basic Commands

## docker build

- [docker build](<https://docs.docker.com/engine/reference/commandline/build/>)
- 새로운 Docker Image를 생성할 때 사용하는 명령어
- Docker Image를 Build하기 위해서는 `Dockerfile`이 필요하다.

```
$ docker build <Directory Path where the Dockerfile exists>
```

- GitHub 등 외부 저장소가 있다면 URL로도 가능하다.

```
$ docker build <URL>
```

### Option: -t

- tag의 약자. 생성되는 이미지의 이름을 지정하기 위해 사용하는 Option이다.

```bash
$ docker build [PATH | URL] -t [Image NAME]
```

## docker run

```bash
$ docker run <image_name>
```

- [docker run](<https://docs.docker.com/engine/reference/run/>)
- Image에 따라 특정 프로세스를 수행하는 Container를 생성하는 명령어
- Image는 실행 명령어와 해당 명령어를 실행하는 데에 필요한 파일 스냅샷을 가지고 있다. docker run을 하게 되면 파일 스냅샷을 포함하여 Container를 구성하고, 실행 명령어를 통해 프로세스를 실행하게 된다.
 
```bash
$ docker run <Image NAME> <command>
```

- <image_name> 뒤에 command 를 전달하게 되면 Image의 command가 아닌 전달 받은 command를 수행하게 된다. 
- 전달하는 command는 당연히 Container 환경 내에서 실행할 수 있어야 한다.

```bash
$ docker run ubuntu ls

bin
boot
dev
etc
home
lib
...
```

### Option: -v

- [Docker Run: VOLUME[Shared Filesystems]](<https://docs.docker.com/engine/reference/run/#volume-shared-filesystems>)
- Container 생성 시 HOST의 파일에 접근하도록 하는 방법도 있다.
- 이렇게 하면 Source Code가 바뀔 때마다 매번 Image를 build 할 필요가 없다.

```bash
# -v [host-src:]container-dest

# select directory
$ docker run -v $(pwd):/usr/src/app <Image NAME>

# or specific file
$ docker run -v $(pwd)/index.js:/usr/src/app/index.js <Image NAME>
```

### Option: -p

- [EXPOSE (incoming ports)](<https://docs.docker.com/engine/reference/run/#expose-incoming-ports>)
- Host의 Port와 Container의 Port를 매핑할 때 사용하는 option이다.
- `3000-3004:3000-3004`와 같이 범위로도 지정이 가능하며, 이때 그 갯수는 동일해야 한다.

```bash
$ docker run -p [ip:hostPort:containerPort | ip::containerPort | hostPort:containerPort | containerPort]
```

### Option: --gpus

- [docker Runtime options with Memory, CPUs and GPUs - GPU](<https://docs.docker.com/config/containers/resource_constraints/#gpu>)
- Container 내에서 GPU에 접근하기 위해서는 `--gpus` Option을 함께 전달해야 한다.


```bash
$ docker run --gpus <Image NAME>
```

### Option: --ipc

- [IPC settings](<https://docs.docker.com/engine/reference/run/#ipc-settings---ipc>)
- IPC란 Inter-Process Communication의 약자로, `--ipc`는  ipc namespace를 설정하는 데에 사용되는 option이다.

```bash
$ docker run --ipc=["host" | "private" | "shareble" | ...  ]
```

### Option: --pid

- [PID settings](<https://docs.docker.com/engine/reference/run/#pid-settings---pid>)
- Container 내에서 Host를 포함하여 전체 System의 Process의 정보를 얻기 위해서는 Container의 PID Namespace를 Host와 맞추어주어야 한다.
- 대표적으로 `htop`, `nvidia-smi`와 같이 Resource Check를 확인할 때 필요한 옵션이다.


```bash
# Share namespace with host
# --pid=["host" | "container:<Conatiner NAME | ID>"]

$ docker run --pid=host <Image NAME>
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
```

- [docker start](<https://docs.docker.com/engine/reference/commandline/start/>)
- docker run = docker create + docker start
- Container의 실행 명령어를 실행하는 단계

### Option: -a

- attach 옵션을 주어야 container의 출력 값을 확인할 수 있다(Attach STDOUT/STDERR and forward signals).

```bash
$ docker start - a <container ID/NAME>
```

## docker exec

- [docker exec](<https://docs.docker.com/engine/reference/commandline/exec/>)
- 현재 실행 중인 Container에 실행 명령어를 전달하는 명령어

```bash
$ docker exec <container ID/NAME> <command>
```

### Options: -it

- `-i`: Interactive
- `-t`: Terminal
- Container 내의 명령어 실행 창에 붙을 수 있다.

```bash
$ docker exec -it <container ID/NAME> <command>
```

## docker stop & kill

- [docker stop](<https://docs.docker.com/engine/reference/commandline/stop/>)
- docker stop과 kill은 모두 현재 실행 중인 Container를 중지하는 명령어

```bash
$ docker stop <container ID/NAME>
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

## docker rmi

- [docker rmi](<https://docs.docker.com/engine/reference/commandline/rmi/>)
- Image를 삭제하는 명령어

```bash
$ docker rmi <image ID/NAME>
```

## docker commit

- [docker commit](<https://docs.docker.com/engine/reference/commandline/commit/>)
- Container를 바탕으로 새로운 Image를 생성하는 명령어

```bash
$ docker commit <Container ID/NAME> <IMAGE NAME>
```

## docker ps

```bash
$ docker ps
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

### Option: -a

- 종료되었거나, 일시 정지 중인 Container도 포함하여 모두 보여준다.

```bash
$ docker ps -a
```

