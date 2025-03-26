altura = float(input("digite sua altura:"))
sexo = input("digite seu sexo:").upper()
if sexo == "MASCULINO":
    peso = (72.7 * altura) - 58
    print("peso ideal masculino:",peso)
else:
    sexo == "FEMININO"
    peso = (62.1 * altura) - 44.7
    print("peso ideal feminino",peso)
