# Crie um programa que pergunte ao usuário um número inteiro e faça a tabuada desse número

tabuada = int(input('Insira um número: '))

for c in range(10):
  print(f'{tabuada}X{c + 1} = {tabuada * (c+ 1)}')