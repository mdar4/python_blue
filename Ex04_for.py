# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o. Mostre também quantos valores pares foram digitados.

soma = 0
par = 0
for c in range(0,6):
  n = int(input('Insira um número: '))
  if n % 2 == 0:
    soma += n
    par += 1
print(f'A soma de numeros pares é {soma} e a quantidade de números par é {par}')