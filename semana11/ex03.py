lista = []
count = 0
count1 = 0
while count1 != 5:
    try:
        valor = int(input("digite numeros"))
        lista.append(valor)
        count1 += 1

    except:
        print(".")
while count != 5:
    try:   
        number = int(input("digite um numero: "))
    except:
        print("valor invalido")

    if number in lista :
        print("NUMERO JA ESTA NA LISTA")

    else:
        lista.append(number)
        count += 1

