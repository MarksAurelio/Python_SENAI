
numero1 = int(input('Informe o número: '))
numero2 = int(input('Informe o número: '))

print('A soma é:', numero1 + numero2)

numeros = [1, 5, 8, 10, 3, 78, 100, 51]

print(max(numeros))
print(min(numeros))
print(len(numeros))
print(sum(numeros))

media = sum(numeros) / len(numeros)

print(media)

# função com 'return'
def media (numeros):
    resultado = sum(numeros) / len(numeros)
    return resultado

media(numeros)
print(media(numeros))

# ou também
resposta = media(numeros)

print(resposta)

# defina uma função com 'return'
def soma (a, b, c):
    soma = a + b + c
    return soma

print(soma(15, 35, 1))

# defina uma função sem 'return'
def saudacao ():
    print('Olá mundo')

saudacao()

def saudacao1(nome):
    print(f'Olá {nome}')

saudacao1('Marks')

# criação de função com parametro opcional sem 'return'
def ola(nome, mensagem='Olá'):
    print(mensagem, nome)

ola('Marks', 'Oi')
ola('Marks')

# função com múltiplo 'return'

def dividir (numero1, numero2):
    resposta = numero1 // numero2
    resto = numero1 % numero2
    return resposta, resto

divisao, resto_divisao = dividir(9, 2)

print(divisao)
print(resto_divisao)

# significado de 'tuple' conjuntos com as '()', não podem ser feita alterações

numeros = (1, 5, 8, 10, 3, 78, 100, 51)

print(type(numeros))

# função abreviada de escrever um função
def soma (a, b, c):
    soma = a + b + c
    return soma

somar = lambda a, b: a + b

print(somar(10, 5))

# parametro ou argumento nomeável
def exibir_informacoes(*args):
    print('Argumentos posicionais: ', args)

exibir_informacoes(1, 4, 'Marks', 'Teste')

def exibir_informacoes2(**args):
    print('Argumentos nomeados: ', args)

exibir_informacoes2(nome='Luciano', idade=30, curso='python')

# Apresentação de Dicionários
# Key : value
# chave : valor
pessoa1 = {'nome': 'Luciano','idade': 30, 'estado_civil': 'casado', 'escolaridade': 'especialista'}

pessoa2 = {'nome': 'Daniel','idade': 19, 'estado_civil': 'noivo', 'escolaridade': 'superior'}
