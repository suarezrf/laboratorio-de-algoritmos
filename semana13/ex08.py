def array(lista):
    for i in range (0,10): 
        numero = int(input(f"{[i + 1]} numero da lista: "))
        lista.append(numero)
    return lista





def inversa(lista):
    lista_inversa = []
    for i in range (9,-1,-1):
        lista_inversa.append((lista[i]))
    return lista_inversa





def main():
    lista = []
    array(lista)
    print(lista)
    inversão = inversa(lista)
    print(inversão)

main()
