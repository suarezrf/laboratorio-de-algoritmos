n1 = int(input("digite o numero 1: "))
n2 = int(input("digite o numero 2: "))
soma = 0
if n1 > n2 :
    for i in range (n2,n1):
        if i % 2 == 0 :
            soma += 1
    print("numeros pares de",n2 , "até", n1, "são", soma)


if n1 < n2 :
    for i in range (n1,n2):
        if i % 2 == 0 :
            soma += 1
    print("numeros pares de",n1 , "até", n2, "são", soma)
