array = []
count = 0



print("1 - Inserir item")
print("2 - Retirar item")
print("3 - Listar itens (um elemento por linha")
print("4 - Retirar todos os itens")
print("5 - Sair")
 
while count != 1:
	opcao = int(input("digite uma das opções: "))

	if opcao == 1:
		
		number = int(input("insira um valor: "))
		array.append(number)
		print(array)
	if opcao == 2:
		print(array)
		exclui = int(input("retire um numero: "))
		array.pop(exclui)
	if opcao == 3:
		for i in range (len(array)):
			print(array[i])


	if opcao == 4:
		print(array)
		array.clear()



	if opcao == 5:
		count +=1
		print(array)

	



