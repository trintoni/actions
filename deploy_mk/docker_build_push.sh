#!/bin/bash
echo "#############################################"
echo "Docker BUILD e PUSH para o HARBOR"
echo "HOSTNAME: ${HOSTNAME}"
echo "WORKSPACE: ${GITHUB_ACTION_PATH}"
echo "USERNAME: ${USER}"
echo "#############################################"
eval $(minikube docker-env)
python3 ${GITHUB_ACTION_PATH}/docker_bp.py

