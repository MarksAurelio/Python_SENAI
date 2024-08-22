# 5. Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print('Ambos números são pares')
else:
    print('Os números são diferentes')
