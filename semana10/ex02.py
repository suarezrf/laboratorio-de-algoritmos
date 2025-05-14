valores = []
valores1 = []
count =  0
soma = 0

while count != 10 :
    try:
        number =  int(input("digite seu numero: "))
        if number in valores:
            print("esse numero ja está na lista, tente novamente")
        else:
            valores.append(number)
            count += 1

        if number > 100:
            valores1.append(number)
            soma += 1


    except:
        print("valor invalido, digite um numero inteiro")

print(valores)
print(valores1)
print(soma, "(essa é a quantia de numeros maiores que 100)")
