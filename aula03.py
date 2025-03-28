#Programa para verificar maioridade

idade = int(input("Digite a sua idade: "))
if idade >=18:
    print("Você é um adulto")
elif idade >=12:
    print("Você é um adolescente")
else:
    print("Você é uma criança")