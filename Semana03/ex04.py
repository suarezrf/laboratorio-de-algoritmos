n1 = float(input("digite a sua primeira nota: ")) 
n2 = float(input("digite a sua segunda nota: ")) 

n3 = (n1 + n2) / 2

if n3 >= 9 and n3 <= 10:
    print("parabens você tirou uma nota A aprovado:) sua nota foi: ",n3 )
    print("sua primeira nota foi: ", n1)
    print("sua segunda nota foi: ", n2)
elif n3 >= 7.5 and n3 <9:
    print("parabens você tirou uma nota B aprovado :)sua nota foi: ",n3) 
elif n3 >= 6 and n3 < 7.5:
    print("parabens você tirou uma nota C aprovado sua nota foi: ",n3)
    print("sua primeira nota foi: ", n1)
    print("sua segunda nota foi: ", n2)
elif n3 >= 4 and n3 < 6:
    print("infelizmente você tirou uma nota D reprovado ;-; sua nota foi: ",n3)
    print("sua primeira nota foi: ", n1)
    print("sua segunda nota foi: ", n2)
elif n3 < 4:
    print("infelizmente você tirou uma nota E reprovado ;-; sua nota foi: ",n3)
    print("sua primeira nota foi: ", n1)
    print("sua segunda nota foi: ", n2)
