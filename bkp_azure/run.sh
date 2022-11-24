pip install azure-identity
pip install azure-mgmt-resource
pip install kubernetes
hostname
# python ${GITHUB_ACTION_PATH}/teste.py
python --version
az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET -t $AZURE_TENANT_ID
az account set --subscription 1163f6b0-6d5e-486b-9299-9a346dd84823
az aks get-credentials --resource-group trinta_aks --name aks_treinamento
docker login trintaacr.azurecr.io --username 00000000-0000-0000-0000-000000000000 --password $TOKEN
kubectl get pods
python ${GITHUB_ACTION_PATH}/deploy.py
