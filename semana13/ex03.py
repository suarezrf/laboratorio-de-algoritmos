def laranjas_maior(n1):
    laranjas = n1 * 0.40
    return laranjas


def laranjas_menor(n1):
    laranjas = n1 * 0.25
    return laranjas

def main():
    print("=-=-=-=-=-=-=--=-==-=-=-=-=-=-=-=-=")
    numero = int(input("digite o numero de laranjas compradas: "))
    if numero >= 12:
        maior = laranjas_menor(numero)
        print(maior)

    elif numero < 12:
        menor = laranjas_maior(numero)
        print(menor)

main()
