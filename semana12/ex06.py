import random
count = 0
lista = []
pares = []
impares = []
soma1 = 0
soma2 = 0
while count != 10:
    valor = random.randint(1, 50)
    lista.append(valor)
    count += 1


for i in range (len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
        soma1 += 1
    else:
        impares.append(lista[i])
        soma2 += 1

print()
print("Lista: ", lista)
print()
print("Numeros pares dentro da lista: ", pares)
print("Quantia de numeros pares: ",soma1)
print()
print("Numeros impares dentro da lista: ", impares)
print("Quantia de numero impares: ",soma2)
