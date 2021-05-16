# Extra informations for Docker

## 1. Cgroup and Namespace

### What is Cgroup and Namespace

- [Anatomy of a Container: Namespaces, cgroups & Some Filesystem Magic - LinuxCon](<https://fr.slideshare.net/jpetazzo/anatomy-of-a-container-namespaces-cgroups-some-filesystem-magic-linuxcon>)에서는 Cgroup과 Namespace에 대해 다음과 같이 언급하고 있다.
  - Cgroup: limits how much you can use
  - Namespaces: limits what you can see
- Cgroup과 Namespace로 개별 Container가 사용할 수 있는 자원을 제한하므로써 여러 Container가 동시에 실행되면서 발생할 수 있는 충돌과 같은 문제들을 해결할 수 있다.

### It's functions of linux kernel

- Cgroup과 Namespace는 Linux Kernel의 기능이지만 Mac/Window 환경에서도 Docker를 사용할 수 있는 이유는 Docker Server는 Linux이기 때문이다. 즉 Docker를 사용한다는 것은 개별 Container의 자원을 관리하는 Linux VM을 실행한다는 것과 동일하다.
- Linux VM을 실행한다는 것은 `docker version` 명령어로 확인이 가능하다.

```bash
# $ docker version
Client: Docker Engine - Community
 ...
 OS/Arch:           darwin/amd64

Server: Docker Engine - Community
 Engine:
  ...
  OS/Arch:          linux/amd64
```

## 2. Redis with Docker

- Redis Server Container 생성하기

```bash
$ docker run redis
```

- Redis Client도 Server Container 내에서 실행하기

```bash
$ docker exec -it <Server Container ID/NAME> redis-cli
```

- 다음과 같이 Server Container의 bash shell에 붙은 후, redis client를 실행해도 동일하다.

```bash
$ docker exec -it <Server Container ID/NAME> [sh, zsh, ...]
$ redis-cli  # in Server Container
```

- Redis 실행 완료

```bash
docker exec -i -t hopeful_napier redis-cli
127.0.0.1:6379> set key1 hello
OK
127.0.0.1:6379> get key1
"hello"
127.0.0.1:6379>
```