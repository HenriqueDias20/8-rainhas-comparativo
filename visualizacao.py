import matplotlib.pyplot as plt
import numpy as np

def mostrar_tabuleiro(solucao):
    tabuleiro = np.zeros((8, 8))
    fig, ax = plt.subplots()
    ax.imshow(tabuleiro, cmap='binary')

    for linha, coluna in enumerate(solucao):
        ax.text(coluna, linha, '♛', ha='center', va='center', fontsize=20, color='red')

    plt.xticks([]), plt.yticks([])
    plt.show()

# Exemplo
if __name__ == "__main__":
    mostrar_tabuleiro([0, 4, 7, 5, 2, 6, 1, 3])
