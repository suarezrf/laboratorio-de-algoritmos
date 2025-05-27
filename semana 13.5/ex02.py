def soma_naturais(n):
    soma = 0
    i = 1
    while i <= n:
        soma += i
        i += 1
    return soma

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 1:
        print("Digite um número natural maior que zero.")
    else:
        resultado = soma_naturais(numero)
        print(f"A soma dos números naturais até {numero} é {resultado}")
main()
