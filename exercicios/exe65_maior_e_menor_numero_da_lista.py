# 65. Escreva um programa que solicite ao usuário uma lista de 5 números 
# e exiba o maior e o menor número dessa lista.

lista = []
for i in range(5):
    numero = int(input(f'Digite o {i+1} número: '))
    lista.append(numero)

maiorNumero = max(lista)
menorNumero = min(lista)

print(f'O maior número é: {maiorNumero}')
print(f'O menor número é: {menorNumero}')
