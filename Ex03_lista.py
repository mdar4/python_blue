# Exercicios de Lista:
# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

soma = 0
lista = [5, 7, 2, 9, 4, 1, 3]
print(f'O tamanho da lista é {len(lista)}\nO maior valor é {max(lista)}\nO menor valor é {min(lista)}\nA soma dos elementos é {sum(lista)}\nEm ordem crescente é {sorted(lista)}\nEm ordem decrescente é {sorted(lista, reverse= True)}')