# Crie um programa que leia dois valores e mostre um menu na tela:

# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

n = 0
soma = 0
mult = 0
maior = 0
n1 = 0
n2 = 0 

while n != 5:
  print('''
  [ 1 ] somar
  [ 2 ] multiplicar
  [ 3 ] maior
  [ 4 ] novos números
  [ 5 ] sair do programa
''')
  n = int(input("Digite sua escolha: "))
  if n == 1:
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    soma = n1 + n2
    print(soma)
  elif n == 2:
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    mult = n1 * n2
    print(mult)
  elif n == 3:
    n1 = int(input('Digite o 1º número: '))
    n2 = int(input('Digite o 2º número: '))
    if n1 > n2:
      print(n1)
    else:
      print(n2) 
  elif n == 4:
    n = int(input("Digite sua escolha: "))