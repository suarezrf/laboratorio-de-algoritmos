#Em um prédio com 10 moradores há três elevadores denominados A, B e C. Para otimizar o sistema de controle dos elevadores, desenvolva um programa em que cada morador informa qual o elevador que utiliza com mais frequência (A, B ou C). 
#O algoritmo deve contabilizar o total de pessoas que usa cada um dos elevadores e mostrar estes totais e suas respectivas porcentagens no final.  

moradores = 0
elevador_A = 0
elevador_B = 0
elevador_C = 0

elevador_Ap = 0
elevador_Bp = 0
elevador_Cp = 0

print("1.Elevador A")
print("2.Elevador B")
print("3.Elevador C")

while moradores != 10:
    opcao = (int(input("Escolha uma das opções: ")))
    moradores += 1 
    if opcao == 1:
        elevador_A += 1
        elevador_Ap += 10
    if opcao == 2:
        elevador_B += 1
        elevador_Bp += 10
    if opcao == 3:
        elevador_C += 1
        elevador_Cp += 10
print("Elevador A foi selecionado",elevador_A ,"vezes.")
print("Elevador B foi selecionado",elevador_B ,"vezes.")
print("Elevador C foi selecionado",elevador_C ,"vezes.")

print("-----------------------------------------------------------")


print("Elevador A foi selecionado",elevador_Ap,"%" ,"das vezes.")
print("Elevador B foi selecionado",elevador_Bp,"%" ,"das vezes.")
print("Elevador C foi selecionado",elevador_Cp,"%" ,"das vezes.")

    

        

    
    
