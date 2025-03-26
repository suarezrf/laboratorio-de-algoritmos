lado1 = int(input("digite o primeiro lado mestre:"))
lado2 = int(input("digite o segundo lado mestre:"))
lado3 = int(input("digite o terceiro lado mestre:"))
if lado1 == lado2 == lado3:
    print("você tem um triângulo equilatero")
elif lado1 == lado2 or lado3 == lado1 or lado3:
    print("você tem um triângulo isósceles")
else:
    print("você tem um triângulo escaleno")
