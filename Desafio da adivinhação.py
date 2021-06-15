#Escreva um programa que pede a senha do usuário, e só sai do 
#looping quando digitarem a senha correta

senha = '123456'
while senha != '123456':
    senha = (input("Digite sua senha: "))
    if senha == '123456':
        print('Conectando...')
    else:
        print('Senha incorreta! Tente novamente.')
