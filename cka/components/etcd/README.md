# ETCD

- 분산 환경에서 key-value 형태의 데이터를 저장할 수 있도록 하는 서비스.
- 쿠버네티스에서는 etcd를 사용하여 `kubectl get` 으로 확인할 수 있는 모든 정보들을 저장한다.
- 쿠버네티스 마스터 노드의 구성요소 중 하나.
- [etcd home page](<https://etcd.io/>)

## Installation

### 1. install go

```
# mac
$ brew install go
```

### 2. etcd clone

```
$ git clone -b v3.5.0 https://github.com/etcd-io/etcd.git
```

### 3. install

```
$ cd etcd
$ ./build.sh
```

### 4. set path

```
export PATH="$PATH:[etcd path]/bin"
```
