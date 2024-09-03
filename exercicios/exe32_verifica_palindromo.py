# verifique se uma string é um palindromo.

texto = input('Informe a sua frase: ').lower().replace(' ','')

if texto == texto[::-1]:
    print('É um palíndromo')