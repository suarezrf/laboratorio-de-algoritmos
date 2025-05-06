soma = 0
soma1 = 0
for i in range (1,11):
    n = int(input("digite uns numero ai: "))

    if n >= 10 and n <= 20:
        soma += 1
    else:
        soma1 += 1

print("=--=-=-=", soma ,"essa e a quantia de numeros que estão no intervalo =-=-=-=-=")
print("=--=-=-=", soma1 ,"essa e a quantia de numeros que não esta no intervalo =-=-=-=-=")
    


