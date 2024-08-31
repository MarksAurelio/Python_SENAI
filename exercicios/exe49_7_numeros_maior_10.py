# 49. Desenvolva um programa que peça ao usuário para inserir 7 números e, ao final, exiba quantos desses números são maiores que 10.

contador = 0
for i in range(7):
    numero = float(input('Digite um número: \n'))
    if numero > 10:
     contador += 1

print('Há', contador, 'números maiores que 10')
