#Faça um algoritmo que simule uma conta bancária:
#1 - Sacar
#2 - Depositar
#3 - Saldo
#4 - Sair

#No início o algoritmo deve solicitar o saldo atual.

contador = 0
saldo = int(input("digite o seu saldo atual: "))

while contador != 4:
    print("sacar")
    print("depositar")
    print("saldo")
    print("Sair")
    opcao = int(input("digite uma das opçôes: "))
    if  opcao == 1:
        sacar = int(input("digite qual quantia em dinheiro você deseja sacar: "))
        saldo -= sacar
        
    elif opcao == 2:
        deposito = int(input("digite a quuantia que você deseja depositar: "))
        saldo += deposito

    elif opcao == 3:
        print(saldo)

    elif opcao == 4:
        print("você saiu do site")
        break
    





