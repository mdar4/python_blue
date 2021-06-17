# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita".
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

perguntas = ["Você telefonou para a vítima?","Você esteve no local do crime?", "Você mora perto da vítima?","Você devia para a vítima?", "Você já trabalhou com a vítima?"]
print(perguntas[0])
r1 = str(input('[S/N]: ')).strip().upper()[0]
print(perguntas[1])
r2 = str(input('[S/N]: ')).strip().upper()[0]
print(perguntas[2])
r3 = str(input('[S/N]: ')).strip().upper()[0]
print(perguntas[3])
r4 = str(input('[S/N]: ')).strip().upper()[0]
print(perguntas[4])
r5 = str(input('[S/N]: ')).strip().upper()[0]

if r1 == 'S' and r2 == 'S' and r3 == 'S' and r4 =='S' and r5 == 'S':
  print("assassino !")
  print("Você foi pego em flagante e foi condenado à 20 anos de prisão.")

elif r1 == 'N' and r2 == 'S' and r3 == 'S' and r4 =='S' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'N' and r3 == 'S' and r4 =='S' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'S' and r3 == 'N' and r4 =='S' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'S' and r3 == 'S' and r4 =='N' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'S' and r3 == 'S' and r4 =='S' and r5 == 'N':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")

elif r1 == 'N' and r2 == 'N' and r3 == 'S' and r4 =='S' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'S' and r3 == 'S' and r4 =='N' and r5 == 'N':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'N' and r2 == 'S' and r3 == 'N' and r4 =='S' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'S' and r3 == 'N' and r4 =='S' and r5 == 'N':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")

elif r1 == 'S' and r2 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r1 == 'S' and r3 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r1 == 'S' and r4 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r1 == 'S' and r5 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r2 == 'S' and r3 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r2 == 'S' and r4 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r2 == 'S' and r5 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r3 == 'S' and r4 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r3 == 'S' and r5 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r4 == 'S' and r5 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r1 == 'N' and r2 == 'N' and r3 == 'N' and r4 =='N' and r5 == 'N':
  print("inocente")
  print("O interrogatório prosseguirá com os demais suspeitos.")
else:
  print(" Comando inválido! Tente novamente.")