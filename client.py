#Aqui vocês irão colocar seu algoritmo de aprendizado
from connection import connect, get_state_reward

socket = connect(2037)

get_state_reward(socket, "jump")