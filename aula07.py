def is_palindromo(texto):
    texto_limpo = ''.join(char.lower()
                          for char in texto
                          if char.isalnum())
    return texto_limpo == texto_limpo[:: -1]
frase = "Subi no onibus"
resultado = is_palindromo(frase)

if resultado:
    resposta = "Sim"
else:
    resposta = "Não"
print(f"A frase '{frase}' é um palíndromo!")