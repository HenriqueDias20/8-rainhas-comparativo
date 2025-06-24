def is_safe(tabuleiro, linha, coluna):
    for i in range(linha):
        if tabuleiro[i] == coluna or \
           abs(tabuleiro[i] - coluna) == abs(i - linha):
            return False
    return True

def resolver(tabuleiro, linha, solucoes):
    if linha == 8:
        solucoes.append(tabuleiro[:])
        return
    for coluna in range(8):
        if is_safe(tabuleiro, linha, coluna):
            tabuleiro[linha] = coluna
            resolver(tabuleiro, linha + 1, solucoes)

def encontrar_todas_as_solucoes():
    solucoes = []
    resolver([0]*8, 0, solucoes)
    return solucoes

if __name__ == "__main__":
    solucoes = encontrar_todas_as_solucoes()
    print(f"{len(solucoes)} soluções encontradas.")
