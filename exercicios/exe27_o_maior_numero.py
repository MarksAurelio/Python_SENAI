# 27. Crie um programa que solicite ao usuário três números e exiba o maior deles.

numero1 = int(input('Digite o primeiro número: \n'))
numero2 = int(input('Digite o segundo número: \n'))
numero3 = int(input('Digite o terceiro número: \n'))

maiorNumero = max (numero1, numero2, numero3)
print('O maior número é', maiorNumero)