def respostas():
    a, b, c = 0, 0, 0
    count = 0
    while count != 20:
        print("1. jornal A")
        print("2. jornal B")
        print("3. jornal C")
        select = int(input("selecione um jornal: "))
        if select == 1:
            a += 1
            count += 1
        elif select == 2:
            b += 1
            count += 1
        elif select == 3:
            c += 1
            count += 1
        else:
            print("opção invalida!")
    print("votos", a ,b ,c,)
    return a, b, c

            
def porcentagem(a, b, c):
    pA = (a / 20) * 100
    pB = (b / 20) * 100
    pC = (c / 20) * 100

    return pA, pB, pC

def main():
    a,b,c = respostas()
    pA,pB,pC = porcentagem(a,b,c)

    print("jornal A teve", pA,"% votos")
    print("jornal B teve", pB,"% votos")
    print("jornal C teve", pC,"% votos")

main()
        


    
