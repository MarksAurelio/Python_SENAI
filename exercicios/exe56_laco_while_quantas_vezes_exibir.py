# 56. Escreva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, 
# e utilize um laço while para exibir a mensagem a quantidade de vezes desejada.

quantidade = int(input('Quantas vezes quer a mensagm seja exibida? \n'))

contador = 1
while contador <= quantidade:
    print('Eu sou programador')
    contador += 1