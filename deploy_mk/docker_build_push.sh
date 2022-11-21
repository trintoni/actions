#!/bin/bash
echo "#############################################"
echo "Docker BUILD e PUSH para o HARBOR"
echo "HOSTNAME: ${HOSTNAME}"
echo "WORKSPACE: ${WORKSPACE}"
echo "USERNAME: ${USER}"
echo "#############################################"
python3 ${GITHUB_ACTION_PATH}/docker_bp.py

