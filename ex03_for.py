# Crie um programa que leia o ano de nascimento de setepessoas. No final, mostre quantas pessoas ainda 
# não atingiram a maioridade e quantas já são maiores

deMaior = 0
deMenor= 0

anoAtual = int(input("Insira o ano atual: "))

for c in range(7):
  idade = int(input('Insira sua idade: '))
  nasc = anoAtual - nasc
  if idade >= 18:
    deMaior += 1
  else:
    deMenor += 1

print(f'Das 7 pessoas {deMaior} são de Maioridade e {deMenor} são de menor.')
