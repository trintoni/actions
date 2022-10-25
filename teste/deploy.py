from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
# Importando uma Classe (Para tratativas com o sistema operacional)
import os
# Classe subprocess para execução de comandos no SO
import subprocess
subprocess.run(["pwd"])
subprocess.run(["ls", "-l"])

idaks = os.environ.get('AZURE_CLIENT_ID')
print("O SECRET É: " + idaks)




# The default credential first checks environment variables for configuration as described above.
# If environment configuration is incomplete, it will try managed identity.
credential = DefaultAzureCredential()


print(credential)