# 6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) 
# e dois números, e realize a operação escolhida.

operadores = str(input('Escolha um dos operadores +, -, * ou /: \n'))
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 + numero2
divisao = numero1 / numero2

if operadores == '+':
    print(numero1, '+', numero2, '=', soma)
if operadores == '-':
    print(numero1, '-', numero2, '=', subtracao)
if operadores == '*':
    print(numero1, '*', numero2, '=', multiplicacao)
if operadores == '/':
    print(numero1, '/', numero2, '=', divisao)


