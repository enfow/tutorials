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
