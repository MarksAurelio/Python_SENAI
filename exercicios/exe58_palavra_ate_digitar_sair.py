# 58. Desenvolva um algoritmo que solicite ao usuário uma palavra 
# e continue pedindo outra palavra até que ele digite "sair".

palavra = ''
while palavra != 'sair':
    palavra = str(input('Digite uma palavra: \n'))
if palavra != 'sair':
    print(f'Você digitou: {palavra}')
    