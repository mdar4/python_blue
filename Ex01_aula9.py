# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já esteja lá dentro, ele não será adicionado. No final, serão exibidos todos os valores 
# únicos digitados, em ordem crescente.

resp = ' '
lista = list()
while True:
  while resp != 'N':
    n = int(input("Digite um número: "))
    lista.append(n)
    resp = str(input('Deseja continuar ?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
      print(sorted(lista))
  break
