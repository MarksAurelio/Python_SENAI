# 43. Desenvolva um programa que pergunte ao usuário quantas vezes ele quer que uma mensagem seja exibida, 
# e depois use um for para imprimir essa mensagem repetidas vezes.

quantidade = int(input('Quantas vezes deseja realizar: '))

for i in range(quantidade):
    print(f'Ok essa é a vez número {i + 1}')

