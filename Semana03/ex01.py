
nome = input("digite o seu nome:")
tempo = int(input("digite a quantos anos você trabalha na empresa:"))
salario = float(input("digite o seu salario:"))
if tempo >= 5 and salario < 2000:
    salariof = salario * 1.10
    print("parabens você merece 10 porcento de aumento no seu ",salariof , nome)
else:
    salariof = salario * 1.05
    print("parabens você merece 5 porcento de aumento no seu ",salariof , nome)

