# ler 5 elementos de um vetor A. Construir um vetor B do mesmo tipo, observando a seguinte lei de formcação:
# '' Todo o elemento de B devará ser o quadrado do elemento de A Correspondente".

vetorA = [1,2,3,4,5,6,7,8,9,10]




def vetor_quadrado(vetorA):
    vetorB = []

    for elemento in vetorA:
        resultado_quadrado = pow(elemento, 2)
        vetorB.append(resultado_quadrado)
    return vetorB

print(vetor_quadrado(vetorA))
