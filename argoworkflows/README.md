# [Argo Workflows](https://argo-workflows.readthedocs.io/en/latest/quick-start/)

[All the examples](https://github.com/argoproj/argo-workflows/tree/main/examples)
[Useful manifests](https://argoproj-labs.github.io/argo-workflows-catalog/)
[Course](https://killercoda.com/argoproj/course/argo-workflows)
Check latest version [here](https://github.com/argoproj/argo-workflows/releases/)
e.g. ```ARGO_WORKFLOWS_VERSION="v3.6.7"```

```bash
kubectl create namespace argo
kubectl apply -n argo -f "https://github.com/argoproj/argo-workflows/releases/download/${ARGO_WORKFLOWS_VERSION}/quick-start-minimal.yaml"
```



Launch UI
```bash
kubectl -n argo port-forward --address 0.0.0.0 svc/argo-server 2746:2746 > /dev/null &
```

Submit workflow
```bash
argo submit hello-world.yaml -n argo --watch
```

See outputs
```bash
argo logs @latest
```

# [Argo Events]

Create namespace to download
```bash
kubectl create ns argo-events

kubectl apply -n argo-events -f https://github.com/argoproj/argo-events/releases/download/v1.9.6/install.yaml

# Install validating webhook (optional)
kubectl apply -n argo-events -f https://github.com/argoproj/argo-events/releases/download/v1.9.6/install-validating-webhook.yaml
```

Eventbus installation

```bash
kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/eventbus/native.yaml
```