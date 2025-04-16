#Faça um programa que receba a idade de dez pessoas e que calcule e mostre a quantidade de pessoas com idade maior ou igual a 18 anos.

pessoas = 0
idade =0 
soma = 0

while pessoas != 10:
    idade =  int(input("digite a sua idade "))
    pessoas += 1
    if idade >= 18:
        soma += 1
        print(soma, "individuo(s) com 18 anos de idade ou mais")
print("até mais, obrigado!")
