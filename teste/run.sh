pip install azure-identity
pip install azure-mgmt-resource
pip install kubernetes
# python ${GITHUB_ACTION_PATH}/teste.py
python --version
python ${GITHUB_ACTION_PATH}/deploy.py
az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET -t $AZURE_TENANT_ID
