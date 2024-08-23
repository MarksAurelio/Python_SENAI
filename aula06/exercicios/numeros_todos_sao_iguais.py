# 40. Escreva um programa que peça ao usuário para inserir três números 
# e verifique se todos são iguais.

numero1 = int(input('Digite o primeiro número: \n'))
numero2 = int(input('Digite o segundo número: \n'))
numero3 = int(input('Digite o terceiro número: \n'))

if numero1 == numero2 == numero3:
    print('Todos os números são iguais')
else:
    print('Um ou mais números é (são) diferentes')
