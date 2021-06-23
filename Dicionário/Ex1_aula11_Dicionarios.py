# 1.    Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
#  Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. 
# Considere que o trabalhador deve contribuir por 35 anos para se aposentar. 

for c in range(1):
  cad = dict()
  cad['nome'] = str(input('Nome: '))
  cad['nascimento'] = int(input(f'Ano do Nascimento de {cad["nome"]}: '))
  cad['carteira'] = int(input('CTPS: '))
  if cad['carteira'] != 0:
    cad['contratacao'] = int(input('Ano de Contratação: '))
    cad['salario'] = float(input('Valor do Salário: '))
    cad['aposentadoria'] = cad['contratacao'] + 35
print()

for k,v in cad.items():
  print(f'{k} é: {v}.')