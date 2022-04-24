# Components of Kubernetes

- [kubernetes components](<https://kubernetes.io/docs/concepts/overview/components/>)

```bash
$ kubectl get pods -n kube-system
NAME                               READY   STATUS    RESTARTS        AGE
coredns-78fcd69978-f64td           1/1     Running   1 (2m44s ago)   10d
etcd-minikube                      1/1     Running   1 (2m44s ago)   10d
kube-apiserver-minikube            1/1     Running   1 (2m44s ago)   10d
kube-controller-manager-minikube   1/1     Running   1 (4d1h ago)    10d
kube-proxy-4j6lx                   1/1     Running   1 (4d1h ago)    10d
kube-scheduler-minikube            1/1     Running   1 (2m44s ago)   10d
storage-provisioner                1/1     Running   3 (90s ago)     10d
```

## Control Plane Components(Master)

- Kube Api Server
- ETCD Cluster
- Kube Controller Manager
- Kube Scheduler

## Node Components(Master)

- Kubelet
- Kube-proxy
- Container Runtime Engine

## 1. Kube Api Server

- 사용자의 Request를 받아서 쿠버네티스의 구성요소들에 적절한 명령을 전달하는 서버.
- pod 생성 Request시 Api Server가 하는 일
  1. Authenticate User
  2. Valiate Request
  3. Retrieve data
  4. Update ETCD
  5. Scheduler
  6. Kubelet -> Build image
  7. Update ETCD

## 2. ETCD Cluster

- 분산 환경에서 key-value 형태의 데이터를 저장할 수 있도록 하는 서비스.
- 쿠버네티스에서는 etcd를 사용하여 `kubectl get` 으로 확인할 수 있는 모든 정보들을 저장한다.
- 쿠버네티스 마스터 노드의 구성요소 중 하나.

## 3. Kube Controller Manager

- 쿠버네티스에는 다양한 component의 상태를 지속적으로 관리하고, 문제가 발생했을 때 적절히 대응하는 Controller가 존재.
  - Node Controller
  - Replication Controller
  - Deployment Controller
  - ...
- Controller Manager는 이러한 Controller들을 관리(Control Loop).
- 예를 들어 Job Controller가 새로운 Task의 존재를 인식하였다면 이를 적절히 처리해 줄 Pod를생성하라는 명령을 Kube Api Server에 전달하여 Pod이 생성되도록 한다.

## 4. Kube Scheduler

- Scheduler의 역할은 어떤 Pod가 어떤 Node에 할당될 것인지 결정하는 것. 실제로 Pod를 생성하거나 하지는 않는다(생성은 Node의 Kubelet이 수행).
- Scheduler는 각 Task의 크기에 따라 적절한 Node를 선택하게 된다.
  - CPU Core, Memory와 같은 Resource, 개별 노드의 중요도(rank) 등을 고려한다.

## 5. Kubelet

- 각 Node의 선장과 같은 역할.
- Node의 작업을 관리하고 Master와 소통한다.
  - Register Node
  - Create Pods
  - Running Containers in the Pod
  - Monitor Node and Pods
  - ...

## 6. Kube-proxy

- Service를 통해 각 Node에 접근할 수 있도록 경로를 Forwarding 해주는 역할 수행. 
