from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient
# Importando uma Classe (Para tratativas com o sistema operacional)
import os
# Classe subprocess para execução de comandos no SO
import subprocess

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
