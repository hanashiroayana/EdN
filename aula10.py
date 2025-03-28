import requests
from time import sleep

def obter_usuario_aleatorio():
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]
        nome = f"{dados['name']['first']}{dados['name']['last']}"
        email = dados['email']
        pais = dados['location']['country']
        return f"Nome: {nome}\nEmail:{email}\nPaís:{pais}"
    except requests.RequestException as e:
        return f"Erro ao obter usuário aleatório: {e}"
    
def main():
    print("Gerando usuário aleatório...")
    sleep(3)
    usuario = obter_usuario_aleatorio()
    print(usuario)
    
if __name__ == "__main__":
    main()
