from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient

credential = DefaultAzureCredential()

client = ResourceManagementClient(
    credential=credential,
    subscription_id="1163f6b0-6d5e-486b-9299-9a346dd84823"
)

for resource_group in client.resource_groups.list():
    print(f"Resource group: {resource_group.name}")

print(f"Successful credential: {credential._successful_credential.__class__.__name__}")




from kubernetes import config , client
from kubernetes.client import Configuration
from kubernetes.client.api import core_v1_api
from kubernetes.client.rest import ApiException
from kubernetes.stream import stream
import re 

pod_namespace = "default"
pod_regex = "treina"
try:
    config.load_kube_config()
    c = Configuration().get_default_copy()
except AttributeError:
    c = Configuration()
    c.assert_hostname = False
Configuration.set_default(c)
core_v1 = core_v1_api.CoreV1Api()

def get_pod_name(core_v1,pod_namespace,pod_regex):    
    ret = core_v1.list_namespaced_pod(pod_namespace)
    for i in ret.items:
        #print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
        pod_name=i.metadata.name
        if re.match(pod_regex, pod_name):
            return pod_name

def check_pod_existance(api_instance,pod_namespace,pod_name):
    resp = None
    try:
        resp = api_instance.read_namespaced_pod(name=pod_name,namespace=pod_namespace)
    except ApiException as e:
        if e.status != 404:
            print("Unknown error: %s" % e)
            exit(1)
    if not resp:
        print("Pod %s does not exist. Create it..." % pod_name)



pod_name=get_pod_name(core_v1,pod_namespace,pod_regex)
check_pod_existance(core_v1,pod_namespace,pod_name)

print("O nome do POD: " + pod_name)



# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))