# 44. Crie um programa que peça ao usuário 10 números e exiba apenas os números pares.

numeros_pares = list()
# numeros_pares = []

for i in range(10):
    numero = int(input('Informe o número: '))

    if numero % 2 == 0:
        numeros_pares.append(numero)

# print('Os números pares são: ', numeros_pares)
print('Os números pares são: ', sorted(numeros_pares)) # sorted: números em ordem crescente

