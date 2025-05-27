def soma_imposto(taxa,custo):
    custoF = custo + (custo * (taxa / 100))
    return custoF



def main():
    taxa = int(input("digite a taxa de imposto: "))
    custo = int(input("digite o valor de um produto: "))
    custo1 = soma_imposto(taxa,custo)
    print(custo1)

main()
