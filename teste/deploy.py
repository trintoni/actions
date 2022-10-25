from azure.identity import DefaultAzureCredential
# Importando uma Classe (Para tratativas com o sistema operacional)
import os
# Classe subprocess para execução de comandos no SO
import subprocess

idaks = os.environ.get('AZURE_CLIENT_ID')
print("O SECRET É: " + str(idaks))

# The default credential first checks environment variables for configuration as described above.
# If environment configuration is incomplete, it will try managed identity.
credential = DefaultAzureCredential()

print(credential)

subprocess.run(["kubectl", "get", "pods"])