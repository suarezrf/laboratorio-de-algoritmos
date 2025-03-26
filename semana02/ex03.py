nascimento = int(input("digite o ano em que você nasceu:"))
idade = 2025 - nascimento
if idade >= 16:
    print("pode votar")
else:
    print("não pode votar")
