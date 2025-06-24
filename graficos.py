import matplotlib.pyplot as plt

algoritmos = ['Backtracking', 'Hill Climbing', 'Simulated Annealing']
tempos = [0.0785, 0.0102, 0.0263] 

plt.figure(figsize=(8, 5))
plt.bar(algoritmos, tempos, color=['blue', 'green', 'orange'])
plt.xlabel('Algoritmo')
plt.ylabel('Tempo de Execução (s)')
plt.title('Comparação de Tempo de Execução entre Algoritmos')
plt.tight_layout()

plt.savefig('relatorio/grafico_tempo.png', dpi=300)
plt.show()
