def maior_item(lista):
    maior = lista[0]
    for i in range (len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior




def menor_item(lista):
    menor = lista[0]
    for i in range (len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor


def main():
    lista = [2,3,4,1,10,9]
    item_M = maior_item(lista)
    item_m = menor_item(lista)
    print("maior numero da lista é: ",item_M)
    print("menor numero da lista é: ",item_m)


main()
