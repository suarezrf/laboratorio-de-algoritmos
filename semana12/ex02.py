lista = []
count= 0
soma = 0

while count != 5:
    try:   
        number = int(input("digite um numero: "))
        lista.append(number)
    except:
        print("digite um numero inteiro!")
    soma += number
    media = soma / 5
    count += 1
print(lista)
print(soma)
print(media)
