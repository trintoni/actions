import docker
client = docker.from_env()

build = client.images.build(path = "./")





