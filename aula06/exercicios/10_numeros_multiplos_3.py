# 64. Crie uma lista com 10 números aleatórios 
# e exiba apenas os números que são múltiplos de 3.

import random

numerosAleatorios = [random.randint(1, 100) for _ in range(10)]

print('Lista de números aleatórios:')
print(numerosAleatorios)

print("\nMúltiplos de 3 na lista:")
for numero in numerosAleatorios:
    if numero % 3 == 0:
        print(numero)

     