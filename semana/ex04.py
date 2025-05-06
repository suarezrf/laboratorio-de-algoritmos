pares = 0
impares = 0
zeros = 0

for i in range (1,11):
    numeros = int(input("digite um numero: "))
    if numeros == 0:
        zeros += 1
    elif numeros % 2 == 0:
        pares += 1
    else:
        impares += 1

print("=-=-= NUMEROS PARES =",pares,"=-=-=-")
print("=-=-= NUMEROS ZEROS =",zeros,"=-=-=-")
print("=-=-= NUMEROS IMPARES =",impares,"=-=-=-")

