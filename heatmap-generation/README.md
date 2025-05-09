# Heatmap Generation

```bash
$ DOCKER_BUILDKIT=1 docker build -t heatmap-generator .
$ docker run -it --rm -v $(pwd)/app:/code/app heatmap-generator
```