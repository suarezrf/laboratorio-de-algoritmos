'''
Escreva um programa que leia um array de 5 elementos 
e determine se todos os elementos são distintos (não há elementos repetidos).
'''
lista = [1,2,3,4,5]
if len(set(lista)) == len(lista):
    print("Todos os elementos são distintos.")
else:
    print("Há elementos repetidos.")
