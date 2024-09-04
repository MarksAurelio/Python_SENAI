# 42. Escreva um algoritmo que solicite ao usuário 5 números inteiros 
# e calcule a soma desses números.
resultado = int()
# for i in range(1, 6):
for i in range(5):
    # numero = int(input(f'Informe o {i} número: '))
    numero = int(input(f'Informe o {i + 1} número: '))
    # resultado = resultado + numero
    resultado += numero

print('A soma dos números é: ', resultado)
