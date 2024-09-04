# 6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) 
# e dois números, e realize a operação escolhida.

numero1 = int(input('Informe o primeiro número: '))

operacao = input('Escolha um dos operadors + - * / ')

numero2 = int(input('Informe o segundo número: '))


match operacao:
    case '+':
        print(f'numero {numero1} {operacao} {numero2}, é: ({numero1} + {numero2})')
    case "-":
        print(f'numero {numero1} {operacao} {numero2}, é: ({numero1} - {numero2})')
    case "*":
        print(f'numero {numero1} {operacao} {numero2}, é: ({numero1} * {numero2})')
    case "/":
        print(f'numero {numero1} {operacao} {numero2}, é: ({numero1} / {numero2})')
    case _:
        print('Operação inválida')

# # ou
# # Definição das oprações em um dicionário
# operacoes = {
#     '+': lambda x, y: x + y,
#     '-': lambda x, y: x + y,
#     '*': lambda x, y: x + y,
#     '/': lambda x, y: x + y,
# }
        
