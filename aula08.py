import random
import string

def gerador_de_senha(tamanho = 8):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha: "))
nova_senha = gerador_de_senha(tamanho_senha)
print(f"Sua senha gerada é: {nova_senha}")