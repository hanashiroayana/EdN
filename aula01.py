def adicionar_pessoa(lista, nome, idade, profissao):
    pessoa = {"nome": nome, "idade": idade, "profissao": profissao}
    lista.append(pessoa)

def exibir_pessoas(lista):
    print("Lista de pessoas cadastradas")
    for pessoa in lista:
        print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Profissão: {pessoa['profissao']}")

pessoas = []


adicionar_pessoa(pessoas, "Ana", 25, "Engenharia")
adicionar_pessoa(pessoas, "Bruno", 30, "Engenheiro")
adicionar_pessoa(pessoas, "Carla", 22, "Médica")

