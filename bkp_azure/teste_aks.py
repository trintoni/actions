from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient

from kubernetes import config, client
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream
import kubernetes.client
import re 
from os import path
import yaml

credential = DefaultAzureCredential()

client = ResourceManagementClient(
    credential=credential,
    subscription_id="1163f6b0-6d5e-486b-9299-9a346dd84823"
)

for resource_group in client.resource_groups.list():
    print(f"Resource group: {resource_group.name}")

print(f"Successful credential: {credential._successful_credential.__class__.__name__}")







# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

with open(path.join(path.dirname(__file__), "nginx-deployment.yaml")) as f:
    dep = yaml.safe_load(f)
    k8s_apps_v1 = client.AppsV1Api()
    resp = k8s_apps_v1.create_namespaced_deployment(body=dep, namespace="default")
    print("Deployment created. status='%s'" % resp.metadata.name)
