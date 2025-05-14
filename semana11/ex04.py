lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
count = 0

while count != 15:
    try:   
        number = int(input("digite um numero: "))
    except:
        print("V")

    if number in lista :
        print("NUMERO JA ESTA NA LISTA")

    else:
        lista.append(number)
        count += 1
