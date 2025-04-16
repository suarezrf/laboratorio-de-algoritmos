contador = 0
pessoa = 0
soma1 = 0 
soma2 = 0

while contador != 3:
    print("1.cadastro")
    print("2.média parcial de idade e altura")
    print("3.sair")
    opcao = int(input("selecione uma das opções: "))

    if   opcao == 1:
        pessoa += 1
        idade = int(input("digite a sua idade: "))
        altura = float(input("digite a sua altura: "))
        soma1 += idade
        soma2 += altura

    elif opcao  == 2:
        media = soma1 / pessoa
        media1 = soma2 / pessoa
        print(media, media1)

    elif opcao == 3:
        print("sua media de altura é", soma2 ,"sua media de idade é", soma1 ," você saiu do nosso sistema até mais.")
        break
    
    else:
        print("opção invalida")
    
    
    
    
