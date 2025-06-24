import random

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
    melhor = tabuleiro[:]
    min_ataques = calcular_ataques(tabuleiro)

    for linha in range(8):
        for nova_coluna in range(8):
            if tabuleiro[linha] == nova_coluna:
                continue
            novo = tabuleiro[:]
            novo[linha] = nova_coluna
            ataques = calcular_ataques(novo)
            if ataques < min_ataques:
                melhor = novo
                min_ataques = ataques
    return melhor

def hill_climbing():
    atual = gerar_estado()
    while True:
        proximo = vizinho(atual)
        if calcular_ataques(proximo) >= calcular_ataques(atual):
            return atual
        atual = proximo

if __name__ == "__main__":
    solucao = hill_climbing()
    print("Solução:", solucao)
    print("Ataques:", calcular_ataques(solucao))
