n1 = float(input("digite a sua primeira nota: ")) 
n2 = float(input("digite a sua segunda nota: ")) 
frequencia = int(input("digite a sua frequência: "))

n3 = (n1 + n2) / 2

if n3 >= 7 and frequencia >= 75:
    print("aprovado!:)")
elif n3>= 4 and frequencia >= 75:
    print("você foi selecionado para o exame!")
elif n3 < 4  or frequencia < 75:
    print("você foi reprovado :-:")
else:
    print("nota ou frequência invalida!")
