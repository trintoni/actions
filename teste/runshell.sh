#!/bin/bash
echo "#############################################"
echo "Informacoes do host (RUNNER)..."
echo "${HOSTNAME}"
echo "${USER}"
echo "${AKS_SECRETS}"
echo "#############################################"

az login -p $AKS_SECRETS -u lulumv@hotmail.com