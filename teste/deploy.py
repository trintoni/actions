from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient
# Importando uma Classe (Para tratativas com o sistema operacional)
import os
# Classe subprocess para execução de comandos no SO
import subprocess


print("AZURE_CLIENT_ID: " + os.environ.get('AZURE_CLIENT_ID'))
print("AZURE_TENANT_IDL: " + os.environ.get('AZURE_TENANT_ID'))
print("AZURE_CLIENT_SECRET: " + os.environ.get('AZURE_CLIENT_SECRET'))

# The default credential first checks environment variables for configuration as described above.
# If environment configuration is incomplete, it will try managed identity.
credential = DefaultAzureCredential()


client = ResourceManagementClient(
    credential=credential,
    subscription_id="1163f6b0-6d5e-486b-9299-9a346dd84823"
)

for resource_group in client.resource_groups.list():
    print(f"Resource group: {resource_group.name}")

print(f"Successful credential: {credential._successful_credential.__class__.__name__}")

from kubernetes import client, config

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))