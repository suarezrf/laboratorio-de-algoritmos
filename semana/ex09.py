a = 0
b = 0
c = 0
print("1.JORNAL A")
print("2.JORNAL B")
print("3.JORNAL C")
for i in range (1,21):

    escolha = int(input("escolha uma das opções: "))

    if escolha == 1 :
        a += 5
    if escolha == 2 :
        b += 5    
    if escolha == 3 :
        c += 5
if a < b and b < c:
    print("JORNAL A ", a,"%" )
    print("JORNAL B ", b,"%" )
    print("JORNAL C ", c,"%" )
elif a < c and c < b:
    print("JORNAL A ", a,"%" )
    print("JORNAL B ", c,"%" )
    print("JORNAL C ", b,"%" )
elif b < a and c > a:
    print("JORNAL A ", b,"%" )
    print("JORNAL B ", a,"%" )
    print("JORNAL C ", c,"%" )
elif  c < a and a < b:
    print("JORNAL A ", c,"%" )
    print("JORNAL B ", a,"%" )
    print("JORNAL C ", b,"%" )
elif  c < b and c < a:
    print("JORNAL A ", c,"%" )
    print("JORNAL B ", b,"%" )
    print("JORNAL C ", a,"%" )
elif b < c and c < a:
    print("JORNAL A ", b,"%" )
    print("JORNAL B ", c,"%" )
    print("JORNAL C ", a,"%" )

