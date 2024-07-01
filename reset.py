## ARQUIVO PARA LIMPAR AS TABELAS DE RESULTADOS
import numpy as np

print("Limpeza das tabelas de resultados. . .")

matriz = np.zeros((96, 3), dtype=np.float64)
np.savetxt('resultado.txt', matriz, fmt="%f")

print('Limpeza concluída.')