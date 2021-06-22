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
perguntas = ["Você telefonou para a vítima?: ",
            "Você esteve no local do crime?: ", 
             "Você mora perto da vítima?: ",
             "Você devia para a vítima?: ", 
             "Você já trabalhou com a vítima?: "]
for c in range(len(perguntas)):
  perguntas[c]= (input(perguntas[c]).strip().upper()[0])
respostas = ["Inocente",
             "Suspeito(a)",
             "Cúmplice",
             "Cúmplice",
             "Assassino(a)"]
culpa = perguntas.count('S')-1
print(f'Você foi julgado como {respostas[culpa]}')
