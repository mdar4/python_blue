# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar 
# quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em 
# uma lista composta.

from random import randint
from time import sleep
# import numpy as np

# j = int(input('Quantidade de Jogos: '))
# n = np.random.randint(1,60, (j,6))
# print(f'''
# Os palpites de jogo são:
# {n}''')

l = list()
j = list()
q = int(input('Jogadas: '))
# Esse for vai gerar os jogos
for c in range(q):
    cont = 0
    l = list()
    # Esse while vai gerar os números dentro dos jogo
    while True:
        num= randint(1,60)
        if num not in l:
            l.append(num)
            cont +=1
        if cont >= 6:
            break
    l.sort()
    j.append(l[:])
print(f'\n{q} jogos sendo sorteados...')
print()
for i, v in enumerate(j):
    print(f'O {i + 1}° jogo sorteado foi: {v}')
    sleep(1)
