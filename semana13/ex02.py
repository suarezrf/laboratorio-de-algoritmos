def valorDobro(n1):
    dobro = n1 * 2
    return dobro


def valorTriplo(n1):
    triplo = n1 * 3
    return triplo


def main():
    numero = int(input("digite numero: "))
    dobro = valorDobro(numero)
    triplo = valorTriplo(numero)
    print("Aqui esta o dobro: ",dobro)
    print("Aqui esta o triplo: ",triplo)


main()
