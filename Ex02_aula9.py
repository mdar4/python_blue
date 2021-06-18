# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas 
# extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

resp = ' '
lista1 = list()
lista2 = list()
lista3 = list()
while True:
  while resp != 'N':
    n = int(input("Digite um número: "))
    lista1.append(n)
    if n % 2 == 0:
      lista2.append(n)
    else:
      lista3.append(n)
    resp = str(input('Deseja continuar ?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
      print(f'Lista completa: {lista1}')
      print(f'Números pares: {lista2}')
      print(f'Números ímpares: {lista3}')
  break
