# Docker Image: Ubuntu without root

- 아래와 같이 기본 ubuntu image를 run하면 root user로 login 된다.

```
docker run -it --rm --name ubuntu ubuntu:20.04 bash
root@3832226f0963:/#
```

- root 가 아닌 일반 유저(ubuntu)로 login 하기 위해서는 Dockerfile에서 user를 생성해주도록 해야 한다.

```
$ make docker-build
...
$ make docker-run
docker run -it --rm ubuntu-no-root bash
ubuntu@4d3180abb56a:/$ ls
```
