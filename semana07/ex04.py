idade = 0
pessoas = 0
contador = 0
soma = 0
soma1 = 0
porcentagem = 0
porcentagem1 = 0

while contador < 7:
    idade = (int(input("digite a sua idade: ")))
    contador += 1
    soma += idade
    soma3 = soma / 7
    if idade >= 18:
        soma1 += 1
    if idade >= 10 and idade <= 30:
        porcentagem += 1
        porcentagem1 = (porcentagem / 7) * 100
    if contador > 6:
        print("a media das idades é ", soma3)
        print("temos", soma1, "maiores de idade.")
        print(porcentagem1, "essa é a porcentagem de pessoas que tem entre 10 e 30 anos de idade.")
