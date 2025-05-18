import random
count = 0
lista = []
pares = []


while count != 10:
    valor = random.randint(1, 100)
    lista.append(valor)
    count += 1


for i in range (len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])

print()
print("lista: ", lista)
print()
print("numeros pares dentro da lista: ", pares)
