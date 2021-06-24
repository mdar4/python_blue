# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

def voto(ano):
  idade = int(input('Idade: '))
  anoAtual = int(input('Ano atual: '))
  ano = anoAtual - idade
  if idade < 16:
    return f'Com {idade} anos, o seu voto é Negado.'
  elif idade >= 16 and idade <= 18:
    return f'Com {idade} anos, o seu voto é Opcional.'
  elif idade >= 70:
    return f'Com {idade} anos, o seu voto é Opcional.'
  else:
    return f'Com {idade} anos, o seu voto é Obrigatório.'
print(voto(ano))
    