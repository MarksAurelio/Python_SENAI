
cavaleiros = ['Seya', 'Aldebaran', 'Aldebaran', 'Shun', 'Shiryu', 'Yoga']

print(cavaleiros)

# adiciona um novo elemento ao final da lista
cavaleiros.append('Ikki')
print(cavaleiros)

# extendendo a lista com outra lista
cavaleiros.extend(['Shina', 'Maryn'])
print(cavaleiros)

# inserir na lista em uma posição específica
cavaleiros.insert(0, 'Athena')
print(cavaleiros)

# remove, exclui um elemento pelo valor
cavaleiros.remove('Shun')
print(cavaleiros)

# pop - exclui o último elemento da lista ou o índice informado
cavaleiros.pop()
print(cavaleiros)

elemento = cavaleiros.pop()
cavaleiros.pop(0)
print(cavaleiros)
print(elemento)

# índice - retorna o índice da primeira ocorrência de um valor procurado
print(cavaleiros.index('Yoga'))

cavaleiros.pop(cavaleiros.index('Yoga'))
print(cavaleiros)

# alterando valor de um elemento da lista
cavaleiros [cavaleiros.index('Ikki')] = 'Ikki de Fênix'
print(cavaleiros)

# contabilizando quantidade de elementos repetidos
print(cavaleiros.count('Aldebaran'))

# sort ordena a lista de forma crescente
frutas = ['morango', 'maça', 'abacaxi', 'kiwi', 'amora', 'umbu', 'laranja','bergamota']

numeros = [9, 5, 81, 100, 33, 21, 2]

frutas.sort()
numeros.sort()
print(frutas)
print(numeros)

frutas.reverse()
numeros.reverse()
print(frutas)
print(numeros)

del frutas[0]
print(frutas)

frutas.clear()
print(frutas)

# deleta definito lista o 'print' não vai funcionar, porque a lista será deletada
del frutas
print(frutas)