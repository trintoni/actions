import docker
import os

client = docker.from_env()

PODNAME = os.environ.get('POD_NAME')
WORKSPACE = os.environ.get('WORKSPACE')
GITHUBWORKSPACE = os.environ.get('GITHUB_WORKSPACE')

build = client.images.build(path = GITHUBWORKSPACE, tag = 'core.harbor.domain/library/' + PODNAME)

client.login(registry='core.harbor.domain', username='admin', password='Harbor12345')
push = client.images.push('core.harbor.domain/library/' + PODNAME)
print(push)


