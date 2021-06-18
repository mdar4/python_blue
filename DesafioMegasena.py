# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar 
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em 
# uma lista composta.

import random
import numpy as np

j = int(input('Quantidade de Jogos: '))
n = np.random.randint(1,60, (j,6))
print(f'''
Os palpites de jogo são:
{n}''')
