# 2. Escreva um programa que peça ao usuário para inserir um número e verifique se o número é maior que 10.

numero = int(input('Informe um número: '))

# if ternário, condicional if e else em uma única linha

resposta = 'Seu número é maior que 10' if numero > 10 else 'menor ou igual 10'

print(resposta)

# ou

if numero > 10:
    print('Seu número é maior que 10')

else:
    print('menor ou igual 10')
    

