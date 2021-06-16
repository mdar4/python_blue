# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# (C) Qual é o nome do produto mais barato.

resp = ' '
#soma = 0
menor = 0
mil = 0
total = 0

while True:
  while resp != 'N':
    nome = str(input('Nome do produto: '))
    preco = float(input("Preço: "))
    total += preco
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
      print(f'O total da compra é R$ {total}')
  break