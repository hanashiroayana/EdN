#Revisão de funções 
def adicionar_pessoa(lista, nome, idade, profissao):
    pessoa = {"nome": nome, "idade": idade, "profissao": profissao}
    lista.append(pessoa)

def exibir_pessoas(lista):
    print("Lista de pessoas cadastradas")
    for pessoa in lista:
        print(f"Nome: {pessoa['nome']:<10}Idade: {pessoa['idade']:<5}Profissão: {pessoa['profissao']}")

def receber_pessoa():
    pessoas = []
    start = input("***Vamos adicionar pessoas?***\nDigite s/n: ").strip().lower()
    while start == "s":
            nome = input("\nNome: ").strip()
            idade = input("\nIdade: ").strip()
            profissao = input ("\nProfissão: ").strip()
            adicionar_pessoa(pessoas, nome, idade, profissao)
            continua = input("Outra pessoa?(s/n):  ").strip().lower()
            if continua !="s":
                 break
    exibir_pessoas(pessoas)

receber_pessoa()
