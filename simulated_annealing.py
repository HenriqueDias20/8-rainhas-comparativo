import random
import math

def gerar_estado():
    return [random.randint(0, 7) for _ in range(8)]

def calcular_ataques(tabuleiro):
    ataques = 0
    for i in range(len(tabuleiro)):
        for j in range(i+1, len(tabuleiro)):
            if tabuleiro[i] == tabuleiro[j] or abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                ataques += 1
    return ataques

def vizinho(tabuleiro):
    novo = tabuleiro[:]
    linha = random.randint(0, 7)
    coluna = random.randint(0, 7)
    novo[linha] = coluna
    return novo

def simulated_annealing(temperatura=1000, resfriamento=0.99):
    estado = gerar_estado()
    ataques = calcular_ataques(estado)

    while ataques > 0 and temperatura > 1e-3:
        novo = vizinho(estado)
        novo_ataques = calcular_ataques(novo)
        delta = novo_ataques - ataques
        if delta < 0 or random.random() < math.exp(-delta / temperatura):
            estado, ataques = novo, novo_ataques
        temperatura *= resfriamento

    return estado

if __name__ == "__main__":
    solucao = simulated_annealing()
    print("Solução:", solucao)
    print("Ataques:", calcular_ataques(solucao))
