def listagem(lista):
    for i in range (0,5):
        numero = int(input("digite numero: "))
        lista.append(numero)
    return lista

def notas(lista):
    soma = 0
    for i in range (len(lista)):
        soma += lista[i]
    print(soma)
    return soma

def media(soma):
    media = soma / 5
    print(media)
    return media


def main():
    lista = []
    listagem1 = listagem(lista)
    soma = notas(lista)
    media1 = media(soma)
    print("Notas: ", listagem1)

    if media1 >= 7:
        print("aprovado 😊")

    elif media1 >= 4 and media1 < 7 :
        print("Recuperação 😐")

    elif media1 < 4:
        print("Reprovado!")
