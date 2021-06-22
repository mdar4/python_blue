# Desafio: Crie um jogo onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi
# escolhido até acertar, entre os palpites diga ao jogador se o número do computador é maior ou menor ao que ele digitou,
# no final mostre quantos palpites foram necessários para vencer.

import random

print('''
Tente vencer adivinhando qual número será escolhido.
Faça a escolha de 0 a 10.
''')

n = random.randint(0,10)
escolha = int(input("Escolha um número de 0 a 10: "))
tentativa = 0

while True:
    if n == escolha:
      print("Parabéns ! Você acertou.")
      tentativa = tentativa + 1
      break
    else:
      print("Não foi dessa vez... Tente novamente !")
      tentativa = tentativa + 1
      if n >= escolha:
        print('O computador jogou um número maior.')
      else:
        print('O computador jogou um número menor.')
      escolha = int(input("Escolha um número de 0 a 10: "))

print(f'Você jogou o número {escolha} e teve {tentativa} tentativas.')
