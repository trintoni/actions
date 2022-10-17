import os

CONSUL_URL_BASE = os.environ.get('INPUT_CONSULURL')

pods = ['b2b_database', 'b2b_api', 'b2b_backend', 'b2b_frontend'] # Criando a lista com conteúdo

print("Imprimindo a lista de PODs: ")
print(pods) # Imprimindo a lista bicycles



container_cpu = [20, 50, 40]


cpu_increase = lambda container_cpu: container_cpu * 0.1 

cpu_increment = list(map(cpu_increase, container_cpu))

print("Adicionando CPU: " + str(cpu_increment))


def exec_command(commands: list, blocked: bool = True) -> tuple:
    """ Exec Command """
    print("##################################################")
    print(f"Exec Command: {CONSUL_URL_BASE}")
    print("##################################################")
    return commands, blocked

print(exec_command(pods))
