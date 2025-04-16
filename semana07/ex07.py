#Faça um programa que receba dez números e usando laços de repetição calcule e mostre a quantidade de números entre 30 e 90.  

n1 = 0
c1 = 0
s1 = 0

while c1 != 10:
    n1 = int(input("digite um numero: "))
    c1 += 1
    if n1 >= 30 and n1 <= 90:

        s1 += 1
    if c1 == 10 :
        print("quantia de numero(s) que estão entre 30 e 90 :", s1)
