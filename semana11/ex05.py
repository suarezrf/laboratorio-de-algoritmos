import random

# Criando o array dos guardiões com forças de ataque
guardioes = []
print("Digite as forças de ataque dos 5 guardiões:")
for i in range(5):
    guardioes.append(int(input("Força do Guardião " + str(i + 1) + ": ")))

# Criando o array dos invasores com forças de defesa (números aleatórios entre 1 e 100)
invasores = random.sample(range(1, 101), 5)  # Garante que os valores não se repetem

# Inicializando o placar
vitorias_guardioes = 0
vitorias_invasores = 0

# Exibindo as forças dos guardiões e dos invasores
print("\nForças dos Guardiões:", guardioes)
print("Forças dos Invasores:", invasores)

# Simulando as batalhas
print("\nResultado das batalhas:")
for i in range(5):
    print("\nBatalha " + str(i + 1) + ":")
    print("Guardião " + str(i + 1) + " com força " + str(guardioes[i]) + " VS Invasor " + str(i + 1) + " com força " + str(invasores[i]))

    if guardioes[i] > invasores[i]:
        print("Resultado: Guardião vence!")
        vitorias_guardioes += 1
    else:
        print("Resultado: Invasor resiste!")
        vitorias_invasores += 1

# Exibindo o placar final
print("\nPlacar final:")
print("Vitórias dos Guardiões: " + str(vitorias_guardioes))
print("Vitórias dos Invasores: " + str(vitorias_invasores))
