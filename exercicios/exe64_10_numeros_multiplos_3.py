# 64. Crie uma lista com 10 números aleatórios 
# e exiba apenas os números que são múltiplos de 3.

lista = []

for i in range(10):
    numero = int(input(f'Digite o {i+1} número: '))
    if numero % 3 == 0:
        lista.append(numero)
print('Os números múltiplos de 3 são: ', end='')
for i in lista:
    print(i, ' ', end='' )
