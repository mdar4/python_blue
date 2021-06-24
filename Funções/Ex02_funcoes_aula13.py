# Faça um programa, com uma função que necessite de um parametro. A função retorna o valor de caractere ‘P’, 
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
# primeira.

def number(n1):
  if n1 > 0:
    return 'Número Positivo.'
  elif n1 == 0:
    return 'Número Neutro.'
  else:
    return 'Número Negativo.'
n1 = int(input('Digite um número: '))
print(number(n1))