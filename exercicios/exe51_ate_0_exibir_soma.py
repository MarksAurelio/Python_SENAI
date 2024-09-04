# 51. Crie um programa que peça ao usuário para inserir números até que ele digite o número 0. Ao final, exiba a soma de todos os números inseridos (exceto o 0).
soma = 0
numero = 1
while numero != 0:
   numero = int(input('Digite um número: \n'))
   soma += numero
   print('A soma dos números é' , soma)
