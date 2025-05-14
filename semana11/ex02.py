numeros = []

for i in range (6):

    num1 = int(input("Digite um elemento: "))
    numeros.append(num1)
    i += 1

constante = float(input("Digite um número constante: "))

resultante = [x * constante for x in numeros]

print(f"Array Resultante: {resultante}")
