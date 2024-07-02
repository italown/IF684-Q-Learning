from connection import connect, get_state_reward
import random as rd
import numpy as np

socket = connect(2037)

matriz = np.loadtxt('resultado.txt')
np.set_printoptions(precision=6)

### PARAMETROS DO AGENTE ###
alpha = 0.20        # Taxa de aprendizagem  [0, 1]
curr_state = 0      # Estado inicial        [0, 95]
curr_reward = -14   # Recompensa inicial    [-14, -1]
gama = 0.9          # Taxa de desconto      [0, 1]
exploracao = 0    # Taxa de exploração    [0, 1]

acoes = ["left", "right", "jump"] # Lista de ações

# Variavel para controlar a quantidade de vezes que os parâmetros são salvos
contador_de_impressoes = 0  

while True:
    print("Estado atual: ", curr_state)

    if exploracao > 0.35:
        exploracao -= 0.001

    if (rd.random() < exploracao):
        indice = rd.randint(0, 2)
        acao = acoes[indice]
        print("Acao escolhida ALEATORIAMENTE: ", acao)
    else:
        indice = np.argmax(matriz[curr_state])
        acao = acoes[indice]
        print("Acao escolhida pelo AGENTE: ", acao)

    estado, recompensa = get_state_reward(socket, acao)
    estado = int(estado[2:], 2)
    next_state = estado
    
    # Equação de Bellman
    matriz[curr_state][indice] = matriz[curr_state][indice] +                                 \
                                alpha*( ( recompensa + (gama * np.max(matriz[next_state]))) - \
                                matriz[curr_state][indice])

    curr_state = next_state
    curr_reward = recompensa

    contador_de_impressoes += 1

    # Salva os parâmetros a cada X estados para melhorar a eficiência
    if contador_de_impressoes == 20:
        np.savetxt('resultado.txt', matriz, fmt="%f")
        contador_de_impressoes = 0