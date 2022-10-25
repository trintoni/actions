pip install azure-identity
pip install azure-mgmt-resource
pip install kubernetes
# python ${GITHUB_ACTION_PATH}/teste.py
python --version
python ${GITHUB_ACTION_PATH}/deploy.py
az login --service-principal -u ceb340c7-ab28-43eb-b5ef-7cf0f90f6190 --password QrP8Q~8RcisVQziJZHlr3qdeG9tKqzHTRdch2djg --tenant bf8ff7cc-d91d-470e-aaee-42bb39736a2a
az account set --subscription 1163f6b0-6d5e-486b-9299-9a346dd84823
az aks get-credentials --resource-group trinta_aks --name aks_treinamento
kubectl get pods
