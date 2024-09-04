#  Desenvolva um algoritmo que peça ao usuário para inserir dois números 
# e verifique se ambos são múltiplos de 5.

numero1 = int(input('Digite o primeiro número: \n'))
numero2 = int(input('Digite o segundo número: \n'))

if numero1 % 5 == 0 and numero2 % 5 == 0:
    print('Ambos são múltiplos de 5')
else:
    print('Ao menos um número não é múltiplo de 5')
