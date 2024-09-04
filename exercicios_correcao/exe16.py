# 16. Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) 
# e exiba o preço correspondente por litro.


combustiveis = [
    {
        'nome' : 'disel',
        'valor' : 6.50
    },
    {
        'nome' : 'gasolina',
        'valor' : 6.17
    },
    {
        'nome' : 'etanol',
        'valor' : 4.45
    }
]

for indice, combustivel in enumerate(combustiveis):
    print(f'{indice} - {combustivel["nome"]}')

escolha = int(input('Informe o número do combustível desejado: '))

print(f'O valor por litro é: {combustiveis[escolha]["valor"]}')
