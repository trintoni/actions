#!/bin/bash
echo "#############################################"
echo "Informacoes do host (RUNNER)..."
echo "${HOSTNAME}"
echo "${USER}"
echo "#############################################"

az login -p $AKS_SECRET -u lulumv@hotmail.com