# 18. Faça um programa que peça ao usuário três números e verifique se todos são positivos.

numero1 = int(input('Digite o primeiro número: \n'))
numero2 = int(input('Digite o segundo número: \n'))
numero3 = int(input('Digite o terceiro número: \n'))

if (numero1 < 0 or numero2 < 0 or numero3 < 0):
    print('Um ou mais números é negativo')
else:
    print('Todos os números são positivos')
