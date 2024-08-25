# 59. Escreva um programa que solicite ao usuário para digitar dois números 
# e verifique se o primeiro é maior que o segundo. 
# Continue pedindo números até que o primeiro número seja maior que o segundo.

while True:
    numero1 = int(input('Digite o primeiro número: \n'))
    numero2 = int(input('Digite o segundo número: \n'))

    if numero1 > numero2:
        print('O primeiro número é maior que o segundo')
    else:
        print('O segundo número é maior que o primeiro')