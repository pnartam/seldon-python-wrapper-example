Docker build

`docker build -t seldon-app .`

Test on local docker

`docker run -p 9000:9000 -it seldon-app`

Deploy on kubernetes

`kubectl apply -f seldon-dep.yaml`

Use below references for setting up kubernetes for seldon

https://www.katacoda.com/farrandtom/scenarios/seldon-core

https://towardsdatascience.com/a-simple-mlops-pipeline-on-your-local-machine-db9326addf31
