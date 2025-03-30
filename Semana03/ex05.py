nome = input("digite o seu nome: ")
r1 = 0
print("responda com sim ou não")


p1 = input("Telefonou para a vítima? ").upper()
if p1 == "SIM":
    r1 += 1 
elif p1 != "NÃO" and p1 != "SIM":
    print("resposta invalida")
    exit()

p2 = input("Esteve no local do crime? ").upper()

if p2 == "SIM":
    r1 += 1 
elif p2 != "NÃO":
    print("resposta invalida")
    exit()

p3 = input("Mora perto da vítima? ").upper()
   
if p3 == "SIM":
    r1 += 1 
elif p3 != "NÃO":
    print("resposta invalida")
    exit()
    
p4 = input("Devia para a vítima? ").upper()

if p4 == "SIM":
    r1 += 1 
elif p4 != "NÃO":
    print("resposta invalida")
    exit()

p5 = input("Já trabalhou com a vítima? ").upper()

if p5 == "SIM":
    r1 += 1 
elif p5 != "NÃO":
    print("resposta invalida")
    exit()

print(nome)
if r1 == 0 or r1 == 1:
    print("você foi classificado como um inocente 😘")

if r1 == 2:
    print("você foi classificado como um suspeito 🤨")

if r1 == 3 or r1 == 4:
    print("você foi classificado como um cumplice 😐")
    
if r1 == 5:
    print("você foi classificado como um assassino 😱😱😱")
