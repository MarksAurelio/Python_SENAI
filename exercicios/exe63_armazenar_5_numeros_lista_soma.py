# 63. Desenvolva um algoritmo que peça ao usuário para inserir 5 números, 
# adicione-os a uma lista 
# e, depois, exiba a soma de todos os números na lista.

lista = []

for i in range(5):
    numero = int(input('Digite o número {}: '.format(i+1)))
    lista.append(numero)
soma = sum(lista)
print('Lista de números: ')
for i in lista:
    print(i)
    
print('A soma dos números é:',soma)
