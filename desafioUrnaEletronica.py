(DESAFIO) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.

# Os códigos utilizados são:

# 1 , 2, 3 - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - José / 2- João / etc)

# 5 - Voto Nulo

# 6 - Voto em Branco

# Faça um programa que calcule e mostre:

# O total de votos para cada candidato;

# O total de votos nulos;

# O total de votos em branco;

# A percentagem de votos nulos sobre o total de votos;

# A percentagem de votos em branco sobre o total de votos.

resp = 9
jose = 0
paulo = 0
joao = 0
rodolfo =0
nulo = 0
branco = 0

while True:
  while resp != 0:
    print('''
    Para votar em digite:

    [1] -José      
    [2]- Paulo     
    [3]- João      
    [4]- Rodolfo   
    [5]- Nulo      
    [6]- Branco    

    OU

    [0]- Para sair
    [7]- Para cancelar
    ''')
    resp = int(input('Opção: '))
    if resp == 1:
      print("Você votou em José.")
      jose +=1
    elif resp == 2:
      print("Você votou em Paulo.")
      paulo +=1
    elif resp == 3:
      print("Você votou em João.")
      joao +=1
    elif resp == 4:
      print("Você votou em Rodolfo.")
      rodolfo +=1
    elif resp == 5:
      print("Você votou Nulo.")
      nulo +=1
    elif resp == 6:
      print("Você votou em Branco.")
      branco +=1
    elif resp == 7:
      int(resp= input('Opção: '))
    elif resp == 0:
      print(f'''
      O total de votos para José foi: {jose}
      O total de votos para Paulo foi: {paulo}
      O total de votos para João foi: {joao}
      O total de votos para Rodolfo foi: {rodolfo}
      O total de votos Nulos foi: {nulo}
      O total de votos em Branco foi: {branco}
      {(jose+paulo+joao+rodolfo) * nulo/100}% foram Nulos
      {(jose+paulo+joao+rodolfo) * branco/100}% foram em Branco
      ''')
  break