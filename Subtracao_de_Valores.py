from random import randint
# A e B são vetores com 20 elementos, C é igual aos 20 elementos subtraidos dos A e B correspondentes.

vetorA = []
vetorB = []
for i in range(20):
    
    vetorA.append(randint(1,100))
    vetorB.append(randint(1,100))

print(vetorA)
print(vetorB)

def vetor_subtracao(vetorA, vetorB):
    vetorC = []

    for elemento in range(20):
        resultado_subtracao = vetorA[elemento] - vetorB[elemento]
        vetorC.append(resultado_subtracao)
    return vetorC

print(vetor_subtracao(vetorA, vetorB))
