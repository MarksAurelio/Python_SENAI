# 5. Faça um programa que solicite ao usuário dois números e verifique se ambos são pares.

numero1 = int(input('Informe o primeiro número: '))
numero2 = int(input('Infomme o segundo número: '))

if numero1 % 2 == 0 and numero2 % 2 == 0:
    print('Ambos os números são pares')
else:
    print('Pelo menos um dos números é ímpar')
    