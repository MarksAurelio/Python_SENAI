frutas = ['acerola', 'maça', 'uva', 'umbu']


def listar_frutas():
    for i in frutas:
        print(i)


def adicionar_fruta(nome):
    frutas.append(nome)


fruta = input('Qual fruta deseja informar: ')
adicionar_fruta(fruta)
listar_frutas()


numeros = [
    [1, 2, 5], 
    [8, 78, 45], 
    [25, 100, 121]
]

for numero in numeros:
    print(numero)

print(numeros[1])

for a, b, c in numeros:
    print(a, b, c)