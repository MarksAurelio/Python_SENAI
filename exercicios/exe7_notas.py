# 7. Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if

nota = int(input('Digite um nota de 0 a 10: \n'))

if nota <= 6:
    print('nota Baixa')
if nota >= 7 <= 8:
    print('nota Média')
if nota >= 8 <= 10:
    print('nota Alta')

