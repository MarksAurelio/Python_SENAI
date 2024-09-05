# 3. Desenvolva um programa que pergunte ao usuário o dia da semana (número de 1 a 7) 
# e exiba o nome do dia correspondente.

diaDaSemana = int(input('Digite um número de 1 a 7: '))

if diaDaSemana == 1:
    print('Domingo')
if diaDaSemana == 2:
    print('Segunda') 
if diaDaSemana == 3:
    print('Terça')
if diaDaSemana == 4:
    print('Quarta')
if diaDaSemana == 5:
    print('Quinta')
if diaDaSemana == 6:
    print('Sexta')
if diaDaSemana == 7:
    print('Sábado') 
else:
    print('Esse número não faz parte dos números solicitados')
    