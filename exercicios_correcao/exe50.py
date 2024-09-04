# 50. Crie um programa que peça ao usuário para inserir um número 
# e, em seguida, exiba os números de 1 até esse número, mas de forma decrescente

numero = int(input('Informe o número: '))

while numero >= 1:
    print(numero, end=' ') 
    numero -= 1

# ou
for i in range(numero, 0, -1):
    print(i, end=' ')

# explicando hierarquia:

texto1 = 'Luciano Lopes'

def saudacao():
    print(f'Olá {texto1} - esse texto veio da função')
    global texto2 # global define uma variável que ainda não foi definida
    texto2  = 'Tia Fran'
    print(f'Olá {texto2} - esse texto veio da função')

saudacao()
print(f'Olá {texto1} - esse texto veio de fora da função')
print(f'Olá {texto2} - esse texto veio de fora da função')
