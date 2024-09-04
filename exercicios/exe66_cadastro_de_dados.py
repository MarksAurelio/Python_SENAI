# 66. Escreva um algoritmo que forneça um menu para o usuário: 1-Cadastrar nome, 
# 2- atualizar o nome, 3, excluir, 4-listar todos os cadastrados, 
# ao final da operação deve dar uma mensagem indicando o resultado da operação 
# e perguntando se deseja realizar
# outra operação, o seu aplicativo apenas deve encerrar quando a opção não for inserida.

cadastro_de_nomes = [] 

def menu_de_cadastro():
    print('Menu:')
    print('1 = Cadastro do nome')
    print('2 = Atualização do nome')
    print('3 = Exclusão do nome')
    print('4 = Lista de todos os cadastros')
    pergunta = int(input('Qual opção desejada? '))
    return pergunta

def cadastrar_nome():
    nome = input('Qual o nome a ser cadastrado? ')
    cadastro_de_nomes.append(nome)
    print('Cadastrado do nome realizado com sucesso!')

def atualizacao_nome():
    nome_anterior = input('Qual o nome para atualização? ')
    if nome_anterior in cadastro_de_nomes:
        relacao_de_nomes = cadastro_de_nomes.index(nome_anterior)
        novo_nome = input('Qual o novo nome? ')
        cadastro_de_nomes[relacao_de_nomes] = novo_nome
        print('Novo nome atualizado com sucesso!')
    else:
        print('Esse nome não foi encontrado!')

def exclusao_nome():
    nome = input('Qual o nome para exclusão? ')
    if nome in cadastro_de_nomes:
        cadastro_de_nomes.remove(nome)
        print('Exclusão do nome realizada com sucesso!')
    else:
        print('Esse nome não foi encontrado!')

def lista_dos_nomes():
    if not cadastro_de_nomes:
        print('Nesta lista não há nomes cadastrados!')
    else:
        print('Lista:')
        for indice, nome in enumerate(cadastro_de_nomes):
            print(f'{indice} - {nome}')

while True:
    pergunta = menu_de_cadastro()
    if pergunta == 1:
        cadastrar_nome()
    elif pergunta == 2:
        atualizacao_nome()
    elif pergunta == 3:
        exclusao_nome()
    elif pergunta == 4:
        lista_dos_nomes()
    else:
        print('Essa opção não é válida. Por favor, escolha outra opção.')
        break

    para_continuar = input('Gostaria de realizar outra operação? (s/n): ')
    if para_continuar.lower() != 's':
        break
    