# 15. Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos)

idade = int(input('Digite uma idade: \n'))

if idade >= 13 and idade <= 17:
    print('Essa pessoa é adolescente')
else:
    print('Essa pessoa não é adolescente')