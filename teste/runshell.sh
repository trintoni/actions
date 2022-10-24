#!/bin/bash
echo "#############################################"
echo "Informacoes do host (RUNNER)..."
echo "${HOSTNAME}"
echo "${USER}"
echo "PASSWORD É: ${AKS_SECRETS}"
echo "#############################################"

az login -p $AKS_SECRETS -u lulumv@hotmail.com