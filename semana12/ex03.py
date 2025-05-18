lista = []
count = 0
posicao_maior = 0
posicao_menor = 0 


while count != 5:
    try:
        number = int(input("digite numero: "))
        count += 1
    except:
        print("numero invalido!")


    lista.append(number)

for i in range (0,5):
    maior = lista[0]
    menor = lista[0]
    if lista[i] > maior:
        maior = lista[i]
        posicao_maior = [i] 
    
    if lista[i] < menor:
        menor = lista[i]
        posicao_menor = [i]
        


print("Sua lista: ", lista)
print()
print("menor numero: ", menor)
print("posição do menor numero: ",posicao_menor)
print()
print("maior numero: ", maior)
print("posição do maior numero: ",posicao_maior)
