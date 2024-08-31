# 28. Escreva um programa que peça ao usuário para inserir uma palavra 
# e verifique se ela tem mais de 5 letras.

palavra = str(input('Digite uma palavra \n'))
numeroLetras = len(palavra)

if numeroLetras > 5:
    print('A palavra', palavra, 'tem mais de 5 letras')
else:
    print('A palavra', palavra, 'tem menos de 5 letras')