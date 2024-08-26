# candidato = int(input('Informe o número do candidato: '))

# if candidato == 13:
#     print('Votou no Lula')
# elif candidato == 22:
#     print('Votou no Bozo')    
# else:
#     print('Candidato inválido')

# match case uma estrutura condicional, alternativa ao if
# abaixo verifica o voto do usuario

# candidato = int(input('Informe o número do candidato: \n'))

# match candidato:
#     case 13:
#         print('votou no Lula \n')
#     case 22:
#         print('votou no Bozo \n')
#     case _:
#         print('opção inválida \n')

# atribuição de valores a uma variável

# numero = 10
# print(numero)

# numero = numero + 10
# print(numero)
# # ou
# numero += 10

# numero = numero - 10
# print(numero)
# # ou
# numero -= 10

# numero = numero * 10
# print(numero)
# # ou
# numero *= 10

# numero = numero / 10
# print(numero)
# # ou
# numero /= 10

# verificando se o numero é par ou ímpar

# numero = int(input('Informe o número '))

# if numero % 2 == 0:
#     print('numero é par')
# else:
#     print('numero ímpar')

# laços de repetição

# for i in range(5):
#     print('Marks')
#     print(i)


# nomes = ['Marks', 'Lucas', 'Arthur', 'Aline', 'Beatriz']

# print(nomes)
# print(nomes[2])

# # for nome in nomes:
# #     print(nome)

# for indice, nome in enumerate(nomes):
#     print(f'Seus nomes são {indice}: {nome}')

# nomes = []

# for i in range(5):
#     nome = input('Informe o seu nome: \n')
#     nomes.append(nome)

# for nome in nomes:
#     print(nome)

# nome = 'Marks'

# for i in nome:
#     print(i)

# While em português Enquanto

numero = None

while numero != 0:
    numero = int(input('Informe o número '))

contador = 1
numero = input('Informe o número ')

while contador < 10:
    print(numero * 2)
    contador +=1

numero = 10
while True:
    numero *= 10
    print(numero)
    if numero > 10000000:
        print(numero)

