# 02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
#  mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3.

for c in range(5):
  t1 = (int(input('Insira um valor: ')), int(input('Insira um valor:')), int(input('Insira um valor:')), int(input('Insira um valor:')))
  print(t1)
  print(f'O número 9 aparece {t1.count(9)}x e o 3 foi digitado na posição {t1.index(3)}')
