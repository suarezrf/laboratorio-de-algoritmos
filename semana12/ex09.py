lista = []
count = 0
soma = 0


while count != 1:
    print("-=-=-=-=-=-=-=-=--=-=-=-=OPÇÕES=-=-=-=-=-=-=--=-=-=-=-")
    print("1_ inserir item")
    print("2_ listar itens")
    print("3_ retirar itens")
    print("4_ retirar todos os itens")
    print("5_ contar quantos itens são maiores que o valor selecionado")
    print("6_ verifique se o numero ja está presente no array")
    print("7_ encontrar o maior e o menor item do array")
    print("8_ sair")
    print("=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    try:
        opcao = int(input("> digite a opções desejada: "))
    except:
        print("opção invalida")
        continue

    if opcao == 1:
        try:    
            numero = int(input("> digite o numero que você deseja inserir na lista: "))
            if numero % 2 == 0:
                lista.append(numero)
            else:
                print("numero impar não é aceito pelo sistema")
        except:
           print("numero invalido")

    elif opcao == 2:
        print(lista)

    elif opcao == 3:
        try:
            print(lista)
            select = int(input("> digite qual item da lista você deseja remover: "))
            lista.pop(select - 1)
            print("item removido")
        except:
            print("numero invalido")

    elif opcao == 4: 
        print(lista)
        lista.clear()
        print("lista depois que tudo é removido")
        print(lista)

    elif opcao == 5:
        soma = 0
        try:
            print(lista)
            op = int(input("> selecione o valor: "))
            for i in range (len(lista)):
                if lista[i] < op:
                    soma += 1
            print("quantia de numeros: ", soma)
        except:
            print("numero invalido")

    elif opcao == 6:
        try:
            numero = int(input("digite um numero: "))
        except:
            print("NUMERO INVALIDO")

        if numero in lista:
            print("Esse numero ja está na lista")
        elif numero not in lista:
            print("Esse numero não está na lista ")        

    elif opcao == 7:
        maior = lista[0]
        menor = lista[0]
        for i in range (len(lista)):
            if lista[i] > maior:
                maior = lista[i]

            if lista[i] < menor:
                menor = lista[i]
        print(maior)
        print(menor)

    elif opcao == 8:
        count += 1
