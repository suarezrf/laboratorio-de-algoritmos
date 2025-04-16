contadorhabitante = 0
somasalario = 0
mulhere10k = 0
maioridade = 0
menoridade = 200 

while contadorhabitante != 10:
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite o seu sexo (m/f): ")
    salario = float(input("Digite seu salário: R$ "))
    somasalario += salario

    if idade > maioridade:
        maioridade = idade

    if idade < menoridade:
        menoridade = idade

    if sexo == "f" and salario <= 10000:
        mulhere10k += 1
    contadorhabitante += 1

mediasalario = somasalario / contadorhabitante

print("Média salarial do grupo: R$ ", mediasalario)
print("Maior idade do grupo:", maioridade)
print("Menor idade do grupo:", menoridade)
print("Quantidade de mulheres com salário até R$10.000,00:", mulhere10k)
