def calcula_gorjeta(conta):
    calculo_gorj = conta*0.15
    return calculo_gorj

def main():
    conta = float(input("Qual o valor da conta? "))
    gorjeta = calcula_gorjeta(conta)
    print(f"Para uma conta de R${conta:.2f}, a  gorjeta é de R${gorjeta:.2f}")

if __name__ == "__main__":
    main()