
verdes = 0
castanhos = 0
azuis = 0
m = 0 
h = 0
cabeloc = 0
cabelol = 0
cabelop = 0
maior_idade = 0
alema = 0

for i in range(1, 16):
    idade = int(input("Digite a idade: "))

    print("1. Mulher")
    print("2. Homem")
    sexo = int(input("Digite uma das opções: "))

    print("1. Castanho")
    print("2. Azul")
    print("3. Verde")
    olhos = int(input("Digite uma das opções: "))

    print("1. Castanho")
    print("2. Loiro")
    print("3. Preto")
    cabelo = int(input("Digite uma das opções: "))


    if cabelo == 1:

        cabeloc += 1

    elif cabelo == 2:

        cabelol += 1
    elif cabelo == 3:

        cabelop += 1


    if olhos == 1:
        castanhos += 1

    elif olhos == 2:
        azuis += 1

    elif olhos == 3:
        verdes += 1

    if sexo == 1:
        m += 1
    elif sexo == 2:
        h += 1

    if idade > maior_idade:
        maior_idade = idade

    if sexo == 1 and 18 <= idade <= 35 and olhos == 3 and cabelo == 2:
        alema += 1


total = 15
porcent_cabeloc = cabeloc / total * 100
porcent_cabelol = cabelol / total * 100
porcent_cabelop = cabelop / total * 100
porcent_castanhos = castanhos / total * 100
porcent_azuis = azuis / total * 100
porcent_verdes = verdes / total * 100
porcent_m = m / total * 100
porcent_h = h / total * 100


print("\n=-=-=-=-=-=-=-=-=-==-=-=- RESULTADOS =-=-=-=-=-=-=--=-=-=-=-=-")
print("A maior idade do grupo é:", maior_idade)
print("=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Porcentagem de pessoas com o cabelo castanho:", porcent_cabeloc)
print("Porcentagem de pessoas com o cabelo loiro:", porcent_cabelol)
print("Porcentagem de pessoas com o cabelo preto:", porcent_cabelop)
print("=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Porcentagem de mulheres no grupo:", porcent_m)
print("Porcentagem de homens no grupo:", porcent_h)
print("-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Porcentagem de pessoas com olhos castanhos:", porcent_castanhos)
print("Porcentagem de pessoas com olhos azuis:", porcent_azuis)
print("Porcentagem de pessoas com olhos verdes:", porcent_verdes)
print("Quantidade de mulheres entre 18 e 35 anos com olhos verdes e cabelo louro:", alema)
