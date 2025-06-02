def soma(n1,n2):
    resultado = n1 + n2
    return resultado

def parametros():
    n1 = int(input("1.  DIGITE PARAMETRO: "))
    n2 = int(input("2.  DIGITE PARAMETRO: "))
    print(n1,"e", n2)
    return n1, n2




def main():
    n1, n2 = parametros()
    resultado = soma(n1,n2)

    print(resultado)




main()
