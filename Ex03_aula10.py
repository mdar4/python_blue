#03 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o programa. No final mostre:
   # Quantas pessoas foram cadastradas
   # Mostre o maior peso
   # Mostre o menor peso
registro = list()
pessoa = list()
maior = menor = n = quant =  0
resp = None

while True:
    while resp != 'N':
        n = int(input('Quantas pessoas deseja registrar?: '))
        for c in range(n):
            pessoa.append(str(input('Nome: ')))
            pessoa.append(float(input('Peso: ')))
            registro.append(pessoa[:])
            pessoa.clear()
            quant +=1
        resp = str(input('Deseja continuar ?[S/N]:')).strip().upper()[0]
    if resp == 'N':
        print(f'{quant} pessoas foram cadastradas.\nEntre elas :\nO maior peso foi:\n{max(registro)}\nO menor peso foi:\n{min(registro)}')
        break
