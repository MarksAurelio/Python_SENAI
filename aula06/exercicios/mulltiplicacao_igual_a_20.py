# 35. Desenvolva um algoritmo que peça ao usuário para digitar dois números 
# e verifique se a multiplicação deles é igual a 20.

numero1 = int(input('Digite o primeiro nome: \n'))
numero2 = int(input('Digite o segundo nome: \n'))

multiplicacao = numero1 * numero2

if multiplicacao == 20:
    print('A multiplicação de ambos os números é igual a 20')
else:
    print('A multiplicação de ambos os números não é igual a 20')
                    