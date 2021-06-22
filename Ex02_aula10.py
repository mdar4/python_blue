# #01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:

# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 

# matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# #02 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna. 
#    C) O maior valor da segunda linha.

c = list()
l = list()
for c in range(3):
    n = int(input('Digite o valor: '))
    print(f'''
    [  {n}  ][  {n}  ][  {n}  ]
    [  {n}  ][  {n}  ][  {n}  ]
    [  {n}  ][  {n}  ][  {n}  ]
    ''')