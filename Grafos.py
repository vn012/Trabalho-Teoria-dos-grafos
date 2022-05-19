import numpy as np
from statistics import mode

texto = open ('grafo.txt')  # Lê um arquivo txt
grafo = texto.readlines()  # readLijnes tranforma cada linha em uma lista

#  Adiciona todos os numeros separadamente num vetor
def nums():
    nums = []
    for i in range(1, len(grafo)):
        nums.append(grafo[i][0:1])
        nums.append(grafo[i][2:3])
    return nums


#  A. Numero de vertices
def n_vertice():
    numeroVertice = (grafo[0])
    return numeroVertice


print(f'Numero de vertices: {n_vertice()} ')


#  B. Numero de arestas
def n_arestas():
    return len(grafo) - 1


print(f"Número de arestas: {n_arestas()} \n ")


#  C. grau Maximo
def grau_maximo():

    return mode(nums())


print(f"Vértice com grau Maximo: {grau_maximo()} \n")


# D. Grau Minimo
def grau_minimo():
    frequencia = []

    for n in nums():
        frequencia.append(nums().count(str(n)))

    grauMinV = []
    for n in range(len(nums())):
        if int(min(frequencia)) == int(frequencia[int(n)]):
            grauMinV.append(nums()[int(n)])

    return grauMinV[0]


print(f"Vértice com grau minimo: {grau_minimo()} \n")


# E. Representação do grafo
def numsvet():
    nums = []
    # Adiciona 2 valores por indice
    for i in range(1, len(grafo)):
        nums.append(grafo[i][0:3])
    return nums
    # print(nums)


def matriz_adj():
    ma = np.full((int(n_vertice()), int(n_vertice())), 0)

    for i in range(int(n_arestas())):
        l = int(numsvet()[i][0:1])-1
        c = int(numsvet()[i][2:3])-1
        ma[l, c] = 1

    for i in range(int(n_arestas())):
        c = int(numsvet()[i][0:1]) - 1
        l = int(numsvet()[i][2:3]) - 1
        ma[l, c] = 1

    return ma


print(f"Matriz de Adjacente: \n {matriz_adj()} ", )
