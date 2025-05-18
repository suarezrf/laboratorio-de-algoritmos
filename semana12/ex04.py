l1 = []
l2 = []
l3 = []
count = 0

while count != 5:
    try:
        number1 = int(input(">  digite os numeros da primeira lista:  "))
        l1.append(number1)
        print()
        number2 = int(input(">  digite os numeros da segunda lista:  "))
        l2.append(number2)
        print
        count += 1

    except:
        print('Numero invalido, digite um numero inteiro!')

    

for i in range (0,5):
    soma = l1[i] + l2[i]
    l3.append(soma)

print()
print(">  primeira lista: ",l1)
print()
print(">  segunda lista:  ",l2)
print()
print(">  soma das duas lista:  ",l3)
