eval $(minikube docker-env)
pip install kubernetes
pip install docker
hostname
# python ${GITHUB_ACTION_PATH}/teste.py
kubectl get pods
python3 ${GITHUB_ACTION_PATH}/k8sdeploy.py
