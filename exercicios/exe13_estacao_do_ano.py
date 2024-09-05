# 13. Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) 
# e exiba a estação do ano correspondente

mesdoAno = int(input('Digite um mês do ano de 1 a 12: \n'))
if mesdoAno >= 3 and mesdoAno <= 6:
    print('Outuno')
elif mesdoAno >= 7 and mesdoAno <= 9:
    print('Inverno')
elif mesdoAno >= 10 and mesdoAno <= 12:
    print('Primavera')
if mesdoAno >= 1 and mesdoAno <= 3:
    print('Verão')
