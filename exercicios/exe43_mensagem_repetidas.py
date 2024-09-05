# 43. Desenvolva um programa que pergunte ao usuário quantas vezes 
# ele quer que uma mensagem seja exibida, 
# e depois use um for para imprimir essa mensagem repetidas vezes.

numero_repeticoes = int(input('Quantas vezes você quer que a mensagem seja exibida? \n'))
mensagem = 'Eu gosto de codificar'

for i in range(numero_repeticoes):
    print(mensagem)

