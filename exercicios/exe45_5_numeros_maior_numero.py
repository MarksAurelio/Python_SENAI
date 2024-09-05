# 45. Escreva um algoritmo que peça ao usuário para inserir 5 números 
# e, ao final, exiba o maior número inserido.

# numero1 = int(input('Digite o primeiro número: \n'))
# numero2 = int(input('Digite o segundo número: \n'))
# numero3 = int(input('Digite o terceiro número: \n'))
# numero4 = int(input('Digite o quarto número: \n'))
# numero5 = int(input('Digite o quinto número: \n'))

# maiorNumero = max (numero1, numero2, numero3, numero4, numero5)
# print('Maior número é', maiorNumero)

# # Ou

maior = None
for i in range(5):
    numero = int(input(f'Informe um número {i + 1} : \n'))

    if maior is None or numero > maior:
        maior = numero

print(f'O maior número é: {maior}')