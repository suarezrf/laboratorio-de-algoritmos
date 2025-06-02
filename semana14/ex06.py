def leitura(lista_A,lista_B):
    for i in range (0, 10):
        numero1 = int(input(f"{i + 1}. digite um numero para a sua primeira lista: "))
        numero2 = int(input(f"{i + 1}. digite um numero para a sua segunda lista: "))
        print()
        lista_A.append(numero1)
        lista_B.append(numero2)
    print("primeira lista", lista_A)
    print("segunda lista", lista_B)
    return lista_A,lista_B

def soma(lista1,lista2):
    lista_C = []
    for i in range(len(lista1)):
        soma1 = lista1[i] + lista2[i]
        lista_C.append(soma1)
    return lista_C

def main():
    lista_A = []
    lista_B = []
    lista1,lista2 = leitura(lista_A,lista_B)
    lista_C = soma(lista1,lista2)
    print("soma das listas", lista_C)




main()
