# 8. Desenvolva um algoritmo que pergunte ao usuário o estado civil (solteiro, casado, divorciado, viúvo) e exiba uma mensagem correspondente.

estadoCivil = str(input('Qual seu estado civil? \n'))

solteiro = 'solteiro'
casado = 'casado'
divorciado = 'divorciado'
viuvo = 'viúvo'

if estadoCivil == solteiro:
    print('Solteiro')
if estadoCivil == casado:
    print('Casado')
if estadoCivil == divorciado:
    print('Divorciado')
if estadoCivil == viuvo:
    print('Viúvo')
else:
    print('Não faz parte da lista informada')

