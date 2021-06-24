# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.

def soma(n1,n2,n3):
  calc = n1 + n2 +n3
  return calc 

def media(soma):
  med = soma / 3
  return f'A média é {med:.1f}'
    
def menu():
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  nota3 = float(input('Nota 3: '))
  somar = soma(nota1, nota2, nota3)
  print(media(somar))
menu()