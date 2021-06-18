# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.

maior = menor = 0
povoado = [['Dara', 20],['Vinicius',21],['Janete',34],['Clara',12],['Duda', 15]]
for pessoa in povoado:
    if pessoa[1] >= 18:
        idade = print(f'{pessoa[0]} é maior de idade.')
        maior += 1
    else:
        idade= print(f'{pessoa[0]} é menor de idade.')
        menor +=1
print(f'{maior} pessoas são de maior.\n{menor} pessoas são de menor.')