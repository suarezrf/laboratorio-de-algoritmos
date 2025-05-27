def ler_numeros():
    numeros = []
    i = 0
    while i < 10:
        valor = int(input(f"Digite o {i+1}º número: "))
        numeros.append(valor)
        i += 1
    return numeros

def remover_repetidos(lista):
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[i] == lista[j]:
                k = j
                while k < len(lista) - 1:
                    lista[k] = lista[k + 1]
                    k += 1
                lista.pop()
            else:
                j += 1
        i += 1
    return lista

def mostrar_lista(lista):
    print("Lista sem números repetidos:")
    for num in lista:
        print(num)

def main():
    numeros = ler_numeros()
    numeros_sem_repetidos = remover_repetidos(numeros)
    mostrar_lista(numeros_sem_repetidos)

main()
