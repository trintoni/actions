#!/bin/bash
echo "#############################################"
echo "Informacoes do host (RUNNER)..."
echo "${HOSTNAME}"
echo "${USER}"
echo "PASSWORD É: ${AKS_SECRET}"
echo "#############################################"

az login -p $AKS_SECRET -u lulumv@hotmail.com