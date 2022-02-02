# Pods, Replica Set, Deployment and Service

## Pods

POD는 사용자가 직접 만들 수 있는 가장 작은 쿠버네티스 객체입니다.

### "One-container-per-Pod"

하나의 POD 내에는 하나의 Application Container만 존재하는 것이 일반적입니다. 하지만 항상 그런 것은 아니며 자원을 공유하기 위해 여러 Application Container가 복수로 동작할 수도 있습니다. 이 경우 Container 간에는 Namespace와 File system 등을 공유할 수 있습니다. 또한 Application Container를 도와주는 Helper Container 도 있습니다. 참고로 Helper Container는 Application Container와 생애주기를 같이합니다.

### Scale up

서비스의 처리량이 늘어나 하나의 POD으로는 적절히 처리할 수 없는 경우, 동일한 POD 내에 새로운 Application Container를 추가하는 대신 동일한 기능을 수행하는 새로운 POD를 새롭게 생성하여 작업을 분담하게 됩니다.

### Pod networking

하나의 Pod은 하나의 IP 주소를 가집니다. 만약 Pod 내부의 Container 간의 네트워킹이 필요한 경우에는 `localhost`로 접근하게 됩니다. File System을 공유하므로 Shared Memory를 통하는 것 또한 가능합니다. Pod 외부의 다른 Pod과 네트워킹을 할 때에는 IP networking을 사용합니다.

### Pod UID

모든 Pod은 고유의 Unique ID를 가집니다. 만약 어떤 Pod이 작업 수행에 실패하여, 재시작 되는 경우에는 기존의 실패한 Pod은 사라지게 되고, 새로운 UID를 가지는 Pod이 새로이 생성됩니다. 즉, 어떠한 경우에도 동일한 UID를 가지는 Pod은 존재하지 않아야 합니다.

### Pod Lifecycle

POD은 다음과 같은 lifecycle phase를 가집니다.

1. Pending: kubernetes cluster가 Pod를 생성할 준비를 하는 단계입니다. Node scheduling, Container image download 등이 Pending Phase에서 이뤄집니다.
2. Running: 특정 Node에 Pod이 할당되어 모든 container가 생성되어 작업을 시작한 단계입니다. 하나라도 동작 중인 Container가 Pod 내에 존재하는 경우 Running Phase로 간주합니다.
3. Succeeded / Failed: Pod 내의 모든 Container들의 작업이 완료된 단계입니다. 하나 이상의 Container 라도 정해진 작업 수행에 실패하는 경우 Failed로 표시됩니다.

만약 Node에 문제가 발생하여 Pod이 정상적으로 작업을 수행하지 못하는 경우에는 Pod을 삭제하고, 새로운 Node에 할당하게 됩니다.

## Workload Resources

Kubernetes Cluster에서는 수 많은 Pod이 각기 다른 Ndoe에서 자신들의 작업을 수행하게 됩니다. 이때 개별 Pod를 하나씩 생성하고 관리한다는 것은 사용자 입장에서 매우 비효율적입니다. Kubernetes에서는 여러 개의 Pod들을 통합적으로 관리하는 여러 Workload Resources를 제공하고 있는데, 대표적으로 `Replica Set`, `Deployment`, `Job & CronJob` 등이 있습니다.

### Replica Set

Replica Set은 특정 POD에 문제가 생기더라도 일정한 개수의 POD를 유지할 수 있도록 합니다. 같은 Replica Set에 포함되어 있는 Pod들은 `metadata.ownerReference` field를 공유합니다.

### Deployment

Deployment는 Replica Set을 관리하는, 보다 높은 수준의 Worlload Resource라고 할 수 있습니다. Deployment는 Replica Set이 제공하는 기능을 모두 포괄하면서 추가적으로 더욱 많은 기능을 제공합니다. 따라서 Replica Set을 직접 사용하지 않고 Deployment를 정의하여 Replica Set을 다루는 것이 좋다고 합니다.

Deployment의 주요 기능은 Replica Set과 Pod을 업데이트하는 것으로, 대표적으로 다음과 같은 것들이 있습니다.

- Rollout Replica Set: 새로운 Replica Set을 생성합니다. 단계적으로 Replica Set은 POD들을 생성하게 됩니다.
- Update Pods: 기능을 유지하면서도 소속된 Pod들의 상태를 업데이트합니다.
- Rollback to an earily status: 과거 상태로 돌아가는 기능도 제공합니다.
- Scaling: 작업 부하가 커지는 경우 작업을 수행하는 Pod들을 추가(horizontal Pod autoscaling)할 수 있도록 합니다.

#### Roll out

Deployment의 Pod template가 변경되면 Deployment는 rollout을 진행합니다. 예를 들어 현재 동작 중인 Deployment에 POD의 Image를 변경하라는 명령을 전달하면, Deployment는 새로운 Image의 POD을 가지는 Replica Set을 새로이 생성하고, 기존 Replica Set을 대체하도록 합니다.

### Job & CronJob

Job은 특정 작업을 수행하는 Pod을 생성해야 할 때 사용하는 Workload Resource 입니다. 특정 횟수만큼 작업이 성공적으로 수행되면 Job은 자신이 생성한 Pod을 모두 제거하게 되는데, 이때 Job은 정의에 따라 차례대로 Pod을 하나씩 생성할 수도, 병렬적으로 Pod을 생성하여 동시에 실행하도록 할 수도 있습니다.

CronJob은 반복적으로 Job을 생성해주는 Workload Resource 입니다. 정의에 따라 한 시간에 한 번, 하루에 한 번과 같은 식으로 Job을 생성하도록 할 수 있습니다.

## References

- [Kubernetes Docs - POD](https://kubernetes.io/docs/concepts/workloads/pods/)
- [Kubernetes Docs - Replica Set](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/)
- [Kubernetes Docs - Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/)
- [Kubernetes Docs - Job](https://kubernetes.io/docs/concepts/workloads/controllers/job/)
- [Kubernetes Docs - CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
