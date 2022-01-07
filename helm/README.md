# Helm

## Commands

### helm install

- helm chart의 인스턴스를 생성하는 명령어이다. helm 식으로 표현하면 release 객체를 생성한다고도 할 수 있다.  postgres helm chart 예제로 확인해보자.

```
# https://artifacthub.io/packages/helm/bitnami/postgresql

$ helm repo add bitnami https://charts.bitnami.com/bitnami
$ helm install test-release bitnami/postgresql   # bitnami/postgresql chart를 사용하여 test-release 라는 이름의 release를 생성하라!
```

- 다음과 같은 에러 메시지가 뜨는 경우가 있다. 이는 연결 가능한  kubenetes cluster가 없어 발생하는 문제이다. kubenetes cluster를 띄워주자.

```
Error: INSTALLATION FAILED: Kubernetes cluster unreachable: Get "https://172.25.0.2:6443/version?timeout=32s": dial tcp 172.25.0.2:6443: i/o timeout
```

- 성공적으로 되었다면 다음과 같이 status 창이 뜬다.

```
NAME: test-postgres
LAST DEPLOYED: Tue Jan  4 16:48:14 2022
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: postgresql
CHART VERSION: 10.14.3
APP VERSION: 11.14.0

** Please be patient while the chart is being deployed **

PostgreSQL can be accessed via port 5432 on the following DNS names from within your cluster:

    test-postgres-postgresql.default.svc.cluster.local - Read/Write connection

To get the password for "postgres" run:

```

- 위의 내용은 다음 명령어로도 확인 가능하다.

```
$ helm status test-postgres
```

- chart가 요구하는 config를 전달하여 release를 생성할 수도 있다.

```
$ helm install -f config.yaml test-postgres bitnami/postgresql
```

- config file의 field는 `$ helm show values [chart-name]` 으로 확인 가능하다.

### helm list

- 생성된 release 객체들을 확인할 수 있는 명령어이다.  

```
NAME            NAMESPACE       REVISION        UPDATED                                 STATUS          CHART                   APP VERSION
test-postgres   default         1               2022-01-04 16:48:14.820085 +0900 KST    deployed        postgresql-10.14.3      11.14.0
```

### helm uninstall

- 생성된 release 객체를 제거하는 명령어이다.

```
$ helm uninstall test-postgres   # test-postgres 라는 이름의 release를 제거하라!
```

- `helm list` 로 확인해보면 제거되었음을 알 수 있다.

```
NAME    NAMESPACE       REVISION        UPDATED STATUS  CHART   APP VERSION
````

### helm repo

- 등록된 저장소를 확인하는 명령어는 `helm repo list` 이다.
- 저장소를 등록하는 명령어는 `helm repo add [location]` 이다.

### helm show

- helm chart의 정보를 확인하기 위해 사용하는 명령어

```
$ helm show all [chart name]  # all information about chart
$ helm show chart [chart name]   # chart's definition
$ helm show crds [chart name]   # charts' CRDs
$ helm show readme [chart name]   # chart's readme
$ helm show values [chart name]   # chart's value
```

## 차트 생성하기

### helm create

- 새로운 차트를 생성해주는 명령어

```
$ helm create [new chart name]
```

- 입력한 이름의 디렉토리가 생성되며, 그 결과는 다음과 같다.

```
# $ tree ./[new chart name]
[new chart name]
├── Chart.yaml   # 차트 정의(이름, 버전 등)
├── charts   # 차트에 종속되는 다른 차트들을 정의하는 곳
├── templates   # 차트에 포함되는 k8s cluster object의 manifesto yaml을 정의하는 곳
│   ├── NOTES.txt
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── hpa.yaml
│   ├── ingress.yaml
│   ├── service.yaml
│   ├── serviceaccount.yaml
│   └── tests
│       └── test-connection.yaml
└── values.yaml
```

## 차트 검증하기

### helm lint

- 구현한 차트에 대해 정적 검사를 해주는 명령어

```
$ helm lint [chart path]
```

## 로컬 차트 실행하기

- `helm install`의 대상으로는 다음 네 가지가 있다.

1. 차트 저장소(e.g. helm hub)
2. 압축 해제된 차트 디렉토리
3. 로컬 차트 압축파일
4. 완전한 URL

- 즉 아래와 같이 helm chart를 정의한 directory를 바로 전달하는 것도 가능하다.

```
$ helm install [chart path]
```

### helm package [chart path]

- 압축 파일로 만들어 관리할 수도 있는데, 압축 파일(.tgz)을 생성하는 명령어는 다음과 같다.

```
$ helm package [chart path]
```
