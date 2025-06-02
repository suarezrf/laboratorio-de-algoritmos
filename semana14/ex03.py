def pesquisa():
    sim, nao = 0 , 0
    for i in range (20):
        print("Você gostou do produto?")
        print("1. sim")
        print("2. não")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        opc = int(input(f"{i + 1}. escolha: "))

        if opc == 1:
            sim += 1

        elif opc == 2:
            nao += 1
        
    return sim, nao






def main():
    sim, nao = pesquisa()
    print(sim,"pessoas escolheram a resposta (sim)")
    print(nao,"pessoas escolheram a resposta (não)")





main()
