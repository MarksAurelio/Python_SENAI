# 39. Crie um algoritmo que peça ao usuário para digitar uma senha e verifique se a senha é "1234".

senha = input('Informe a senha: ')

if senha == '1234':
    print('Senha correta!')


# ou
senha = str()

while senha != '1234':
    senha = input('Informe a senha: ')
    