# 44. Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

numeros_pares = []

for i in range(10):
   numero = int(input('Digite um número: \n'))
   if numero % 2 == 0:
       numeros_pares.append(numero)
       
print('Os números pares digitados foram', numeros_pares)
 