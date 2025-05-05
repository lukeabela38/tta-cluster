# tta-cluster

# Monitoring

## [SonarQube](https://sonarcloud.io/summary/overall?id=lukeabela38_tta-cluster&branch=main)

# Installation

## [Multipass](https://github.com/southsidedean/intro-to-multipass-macos)
```bash
$ brew install --cask multipass
```

## [Microk8s](https://microk8s.io/docs/install-macos)
```bash
$ brew install ubuntu/microk8s/microk8s
$ microk8s install
```

## Docker

```bash
$ DOCKER_BUILDKIT=1 docker build -t python-fast-api .
$ docker run -it --rm -v $(pwd)/app:/code/app -p 3000:3000 python-fast-api
```

```bash
$ docker tag DOCKER_IMAGE_ID lukeabela56/tta-cluster-app:v0.0.1
$ docker push lukeabela56/tta-cluster-app:v0.0.1
```

## Kubernetes

### [Kubectx](https://formulae.brew.sh/formula/kubectx)

```bash
$ brew install kubectx
```

### [Kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-macos/#install-with-homebrew-on-macos)

```bash
$ brew install kubectl
```

### [Minikube](https://matthewpalmer.net/kubernetes-app-developer/articles/guide-install-kubernetes-mac.html)

```bash
$ curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.27.0/minikube-darwin-amd64 &&\
$ chmod +x minikube &&\
$ sudo mv minikube /usr/local/bin/
$ minikube start
```

