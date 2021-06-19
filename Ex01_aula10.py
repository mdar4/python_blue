# 1° Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for 
# 2° Com if, verifique quais clientes são maiores de idade e quais são menores de idade.
# 3° mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' 
# 4° e  também quantos são maiores e quantos são menores de idade.

povoado = list()
pessoa = list()
maior = menor = 0
for c in range(5):
    pessoa.append(str(input('Nome: ')))
    pessoa.append(str(input('Idade: ')))
    povoado.append(pessoa[:])
    pessoa.clear()
for i in povoado:
    if i[1]>= 18:
        print(f'{p[0]} é maior de idade.')
        maior +=1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'{maior} são de maior e {menor} são de menor.')