# 16. Desenvolva um programa que peça ao usuário um tipo de combustível 
# (gasolina, etanol, diesel) 
# e exiba o preço correspondente por litro

combustivel = str(input('Escolha o tipo de combustível gasolina, etanol ou disel: \n'))

gasolina = 'gasolina'
etanol = 'etanol'
disel = 'disel'

if combustivel == gasolina:
    print('O litro da Gasolina é R$5,99')
elif combustivel == etanol:
    print('O litro do Etanol é R$4,59')
elif combustivel == disel:
    print('O litro do Disel R$ 3,99')
else:
    print('Item não está na lista de combustivéis')

