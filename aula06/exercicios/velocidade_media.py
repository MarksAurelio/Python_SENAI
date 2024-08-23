# 12. Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

mododeTransporte = str(input('Escolha um modo de transporte carro, bicicleta e a pé: \n'))

if mododeTransporte == 'carro':
    print('O percurso a carro é 100 km/h')
if mododeTransporte == 'bicicleta':
    print('O percurso de bicicleta é 25 km/h')
if mododeTransporte == 'a pé':
    print('O percurso a pé é 3,6 km/h')

