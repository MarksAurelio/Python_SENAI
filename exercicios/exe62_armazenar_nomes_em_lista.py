# 62. Escreva um programa que solicite ao usuário para inserir 3 nomes 
# e armazene-os em uma lista. 
# Em seguida, imprima a lista completa.

lista = []

for i in range(3):
    nome = input('Digite o nome {}: '.format(i+1))
    lista.append(nome)

print('lista de nomes: ')
for nome in lista:
    print(nome)
    