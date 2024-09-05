# 46. Desenvolva um programa que pergunte ao usuário para inserir 10 números 
# e, ao final, exiba a média dos números inseridos.

soma = 0
for i in range(10):
    numero = float(input(f'Informe o número {i + 1} : \n'))
    soma += numero

media = soma / 10
print(f'A média dos números é {media}')
