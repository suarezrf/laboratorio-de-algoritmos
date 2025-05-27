
def eh_primo(n):
    if n < 2:
        return False
    i = 2
    while i <= n // 2:
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    numero = int(input("Digite um número inteiro: "))
    if eh_primo(numero):
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")

main()
