# numero1 = 10
# numero2 = 10
# # operador maior >
# print(numero1 > numero2)
# print(numero2 > numero1)

# # operador menor <
# print(numero1 < numero2)
# print(numero2 < numero1)

# # operador igual =
# print(numero1 == numero2)
# print(numero1 >= numero2)
# print(numero1 <= numero2)
# print(numero1 != numero2)

# idade = int(input('Informe sua idade: \n'))

# if (idade > 120):
#     print('Idade invalida')
# elif (idade >= 18):
#     print('Maior de idade')
# elif (idade < 0):
#     print('Ainda não nasceu')
# else:
#     print('Menor de idade')    

# idade = int(input('Informe sua idade: \n'))

'''
if(idade >= 18):
    print('Pode assistir o filme')
elif(idade >= 16):
    acompanhado = input('Esta acompanhando de adulto sim o não? \n')
    if (acompanhado == 'sim'):
        print('Pode assistir')
    else:
        print('Não pode assistir')
else:
    print('Não pode assistir')
'''

'''
idade = int(input('Informe sua idade: \n'))
if (idade < 18):
    acompanhado = input('Esta acompanhando de adulto sim ou não? \n')
    if (acompanhado == 'sim'):
        print('pode assistir')
    else:
        print('não pode assistir')
else:
    print('pode assistir')
'''
# AND
# alladin = input('Alladin apareceu? \n')
# jasmine = input('Jasmine apareceu? \n')

# if (alladin == 'sim') and (jasmine == 'sim'):
#     print('Love a noite inteira')
# else:
#     print('Não rolou o encontro')

# OR
# alladin = input('Alladin apareceu? \n')
# jasmine = input('Jasmine apareceu? \n')

# if (alladin == 'sim') or (jasmine == 'sim'):
#     print('Love a noite inteira')
# else:
#     print('Não rolou o encontro')

# NOT
alladin = input('Alladin apareceu? \n')
jasmine = input('Jasmine apareceu? \n')

if not((alladin == 'sim') or (jasmine == 'sim')):
    print('Love a noite inteira')
else:
    print('Não rolou o encontro')




