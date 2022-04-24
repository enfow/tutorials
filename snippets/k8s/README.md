# k8s

## commands

### kubectl port-forward

- [kubectl port-forward](<https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#port-forward>)
- 로컬 포트를 Kubenetes cluster 객체의 포트로 포트포워딩 할 때 사용된다.

```
# pod/mypod를 local port 5000, 6000과 연결하는 명령어
$ kubectl port-forward pod/mypod 5000 6000

# deployment/mydeployment를 local port 5000, 6000과 연결하는 명령어
$ kubectl port-forward deployment/mydeployment 5000 6000

# svc/mysvc를 local port 5000, 6000과 연결하는 명령어
$ kubectl port-forward svc/mysvc 5000 6000
```

- k8s cluster 객체의 포트를 지정할 수도 있다.

```
# 로컬포트 8888을 pod/mypod의 포트 5000과 연결하는 명령어
$ kubectl port-forward pod/mypod 8888:5000
```

- IP를 지정할 수도 있다.

```
# 로컬과 10.19.21.23의 포트 8888을 pod/mypod의 포트 5000과 연결하는 명령어
$ kubectl port-forward --address localhost,10.19.21.23 pod/mypod 8888:5000
```
