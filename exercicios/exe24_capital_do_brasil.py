# 24. Desenvolva um algoritmo que pergunte ao usuário o nome de uma cidade 
# e verifique se é a capital do Brasil.

nomedaCidade = input('Digita o nome de uma cidade: \n')
nomedaCidade = nomedaCidade.lower()

if nomedaCidade == 'brasília':
    print('Está correto Brasília é a capital do Brasil')
else:
    print('Está incorreto essa cidade não é a capital do Brasil')
