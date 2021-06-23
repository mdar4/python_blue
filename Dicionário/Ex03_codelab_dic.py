# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.

dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]} : '))
if dados['media'] >= 7:
  dados['situcao'] = 'Aprovado'
elif 5 <= dados['media'] < 7:
  dados['situacao'] = 'Em recuperação'
else:
  dados['situacao'] = 'Reprovado'
print()
for k, v in dados.items():
   print(f'{k} é igual a {v}')