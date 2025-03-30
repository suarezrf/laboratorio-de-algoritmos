morangokg = float(input("digite a quantia de kg de morango que você deseja: "))
macakg =float(input("digite a quantia de kg de maçã que você deseja: "))

morango_s = 2.50
morango_c = 2.20
maca_s = 1.80
maca_c = 1.50

if morangokg <= 5:
    morangov = morangokg * morango_s
else:
    morangov = morangokg * morango_c

if macakg <= 5:
    macav = macakg * maca_s
else:
    macav = macakg * maca_c
    
valor_total = macav + morangov 

if macakg + morangokg > 8 or valor_total > 25:
   valorp = valor_total * 0.90


print(morangokg, macakg)
print("o valor total de maçâs foi:",macav)
print("o valor total de morangos foi:",morangov)
print("valor total a ser pago é:",valorp)
