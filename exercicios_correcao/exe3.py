# 3. Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) e exiba o nome do dia correspondente.

dias_semana = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']

for indice, dia in enumerate(dias_semana):
    print(f'{indice + 1} - {dia}')

dia = int(input('Informe um número de 1 a 7: '))

print(f'O dia que vocé escolheu foi: {dias_semana[dia-1]}')
