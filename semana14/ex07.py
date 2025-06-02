# Crie um algoritmo que:
# Peça ao usuário para digitar 10 números inteiros e armazene-os em um array.
# Utilize uma função para verificar se cada número é primo.
# Exiba todos os números primos encontrados no array.
# Requisitos:
# Use for para percorrer o array.
# Use uma função eh_primo(n) que retorne True ou False


def numeros(lista):
    for i in range (0,10):
        numero = int(input("digite um numero para a sua lista: "))
        lista.append(numero)
    print(lista)
    return lista 

def primo(numero):
    divisor = 0
    for i in range (1,numero + 1):
        if numero % i == 0:
            divisor += 1
    if divisor == 2:
        print(numero, "true")
        return True 
    else:
        print(numero ,"false")
        return False

            
    

def main():
    lista = []
    lista1 = numeros(lista)
    lista_primos = []
    for i in range (len(lista1)):
        cu = primo(lista1[i])
        if cu == True:
            lista_primos.append(lista[i])
    print(lista_primos)

main()
