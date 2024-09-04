# 1. Crie um programa que pergunte ao usuário um número de 1 a 3
# e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").

numeros_extenso = ['um', 'dois', 'três']

numero = int(input('Informe um número de 1 a 3: '))

print(f'Seu número por extenso é: {numeros_extenso[numero-1]}')

# ou 

numeros_extenso = ['um', 'dois', 'três']

numero = int(input('Informe um número de 1 a 3: '))

if numero < 1 or numero > 3:
    print('número inválido')

else:
    print(f'Seu número por extenso é: {numeros_extenso[numero-1]}')
    

