# Pods, Replica Set, Deployment and Service

## Pods

- 사용자가 직접 만들 수 있는 가장 작은 쿠버네티스 object

### Multiple Container in a Pod

- 하나의 Pod에는 하나의 Application Container만 존재.
- Application Container 외에도 Helper Container가 같이 존재.
- Helper Container의 생명주기는 Application Conatainer와 동일.

### Scale up

- Application에 대한 처리량이 늘어나 하나의 Application으로는 적절히 처리할 수 없는 경우, POD 내에 새로운 Application Container를 생성하지 않는 대신 새로운 POD를 생성하여 분담하여 처리하게 된다. 

### Commands

- 특정 이미지를 실행하는 POD 생성 및 실행

```
$ kubectl run [POD NAME] --image [IMAGE NAME TO RUN]
```

- 현재 생성되어 있는 POD 확인

```
$ kubectl get pods
```

## Replica Set

- POD의 집합
- 특정 POD에 문제가 생기더라도 지속적인 서비스가 가능하도록 일정 개수의 POD를 유지할 수 있도록 해줌
- Replica Set을 사용하면 여러 개의 Node에 존재하는 POD를 함게 관리할 수 있다.
- Replica Set은 Replication Controller를 대체(신기술).

## Deployment

## Service

