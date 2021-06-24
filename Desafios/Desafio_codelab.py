# DESAFIO: Crie um programa que leia nome, sexo biologico e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:

# A) Quantas pessoas estão cadastradas.

# B) A média da idade.

# C) Uma lista com as mulheres.

# D) Uma lista com as idades que estão acima da média.

# OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.

resp = None
mlist = list()
acimaDaMedia = list()
cad = mulher = soma_idade = 0

while True:
  while resp != 'N':
    dados = dict()
    pessoa = list()
    media = list()
    cad += 1
    nome = str(input('Nome: '))
    dados['nome'] = nome
    sexob = str(input('Sexo Biológico [F/M]: ')).strip().upper()[0]
    dados['sexob'] = sexob
    # if dados['sexob']!= 'F' and dados['sexob']!= 'M':
    while dados['sexob'] not in 'FM': # Tratativa de erro. O código só seguirá em frente se o usuário responder corretamente.
      print('Comando Inválido !')
      sexob = str(input('Sexo Biológico [F/M]: ')).strip().upper()[0]
      dados['sexob'] =  sexob
    idade =  int(input('Idade: '))
    dados['idade'] = idade
    soma_idade += idade
    media = soma_idade / cad
    if idade > media:
      acimaDaMedia.append(dados['idade'])
    pessoa.append(dados.copy())
    if dados['sexob'] == 'F':
      mlist.append(dados['nome'])
      mulher += 1
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
  if resp == 'N':
    break
print()
print(f'Quantidade de Cadastros: {cad}.')
print(f'Quantidade de Mulheres são: {mulher}\nSendo elas: {mlist}.')
print(f'A Média de idade é {int(media)}')
print(f'As idades à cima da média são: {acimaDaMedia}')
