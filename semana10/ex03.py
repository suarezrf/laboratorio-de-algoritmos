lista1 = []
count = 0

while count != 10:
        try:   
            number = int(input("digite um numero: "))
        except:
            print("VSFD PUNTELL")

        if number in lista1 :
              print("NUMERO JA ESTA NA LISTA")

        else:
            lista1.append(number)
            count += 1
for i in range (len(lista1)):
    if lista1[i] % 2 == 0:
        print(lista1[i])
        print(lista1[i],i)
