vetorA = []
vetorB = []
count = 0

while count != 10:
    number = int(input("digita um numero: "))
    vetorA.append(number)
    count += 1
for i in range (9,-1,-1):
    vetorB.append(vetorA[i])
print(vetorA)
print(vetorB)
