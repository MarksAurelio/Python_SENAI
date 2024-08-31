# 36. Crie um programa que solicite ao usuário um número de 1 a 12 
# e exiba o mês correspondente.

numero1 = int(input('Digite um número de 1 a 12: \n'))

if numero1 == 1:
    print('Janeiro')
elif numero1 == 2:
    print('Fevereiro')
elif numero1 == 3:
    print('Março')
elif numero1 == 4:
    print('Abril')
elif numero1 == 5:
    print('Maio')
elif numero1 == 6:
    print('Junho')
elif numero1 == 7: 
    print('Julho')
elif numero1 == 8:
    print('Agosto')
elif numero1 == 9:
    print('Setembro')
elif numero1 == 10:
    print('Outubro')
elif numero1 == 11:
    print('Novembro')
elif numero1 == 12:
    print('Dezembro')
else:
    print('Esse número não faz parte da lista solicitada')

