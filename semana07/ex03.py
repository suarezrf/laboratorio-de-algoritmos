#Fazer um algoritmo que leia diversos números e mostre quantas vezes o número 10 foi digitado.
# O laço de repetição deve parar quando o usuário digitar 0.

contador = 0
soma = 0

while contador == 0:
    n1 = int(input("digite um numero entre 0 e 10: "))
    if n1 == 10:
        soma += 1
        print("você digitou o numero 10:", soma ,"vez.")
    elif n1 == 0:
        print("você saiu do sistema😢.")
        break
