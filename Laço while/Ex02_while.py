# Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

resp = ' '
dMaior = 0
sexo = ' '
homem = 0
mulher = 0

while True:
  while resp != 'N':
    idade= int(input("Digite sua idade: "))
    if idade > 18:
      dMaior += 1
    sexo = str(input("Digite seu sexo biológico [F/M]: ")).strip().upper()[0]
    if sexo == 'M':
      homem += 1
    elif sexo == 'F':
      if idade >= 18:
        mulher += 1
    else:
      print('Comando inválido !')
    resp = str(input('Deseja continuar ?[S/N]: ')).strip().upper()[0]
    if resp == 'N':
      print(f'{dMaior} pessoas tem mais de 18 anos,\n{homem} homens foram cadastrados e {mulher} mulheres são maiores de idade.')
  break
