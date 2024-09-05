

texto = 'Marks Aurelio    '

texto2 = texto.capitalize()
# capitalize muda o primeiro caracter da string para maiusculo
print(texto.capitalize())
print(texto2)

# lower padroniza a string em minusculo

nome = 'luCiAno LoPes FerReiRa'
nome2 = 'luciano lopes ferreira'
print(nome.lower())

if nome.lower() == nome2.lower():
    print('São iguais')
else:
    print('Não são iguais')

# upper padroniza uma string em maiusculas

print(nome.upper())

# replace muda um padrão de caracteres de uma string

silvano_sales = 'coração coração cabeção'

# silvano_sales2 = silvano_sales.replace('ç','c').replace('ã','a')

print(silvano_sales.replace('çã','ca'))

# strip é uma forma de remover caracteres em branco no final e no inicio de uma string

jack_stripador = '               removendo espaços de uma string         '

print(jack_stripador)
print(jack_stripador.strip())

# split divide uma string com base no espaço entre as palavras, se no caso as palavras tiverem '-' entre elas, ele considera isso a referència em vez do espaço.

string_espalhada = 'Marks-Aurelio'

print(string_espalhada)
print(string_espalhada.split('-'))

# join transforma os elementos de uma lista em uma string
# concatena strings

nome_lista = ['Marks', 'Aurelio', 'Araujo']

print(' '.join(nome_lista))

print('-'.join(nome_lista))

dominio = '@aluno.senai.br'
print('marks.aurelio'+dominio)

# slice maipula string por indice

cidade = 'Recanto das Emas, cidade do povo'

print(cidade[5:])
print(cidade[:12])
print(cidade[12:16])
print(cidade[:-1])
print(cidade[::-1])

palindromo = 'Arara'

if palindromo.lower() == palindromo[::-1].lower():
    print('é palindromo')
else:
    print('não é palindromo')

    