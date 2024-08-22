# 22. Escreva um programa que peça ao usuário para inserir dois números e verifique se o primeiro é maior que o segundo.

numero1 = int(input('Digite o primeiro número: \n'))
numero2 = int(input('Digite o segundo número: \n'))

if numero1 > numero2:
    print('O primeiro número é maior que o segundo')
else:
    print('O primeiro número é menor que o segundo')