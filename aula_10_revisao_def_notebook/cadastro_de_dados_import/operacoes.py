nomes = []

def menu():
    opcoes = ['Cadastrar nome', 'Atualizar nome', 'Excluir nome', 'Listar nome']

    for indice, opcao in enumerate(opcoes):
        print(f'{indice +1} - {opcao}')
def listar_nomes():
    for indice, opcao in enumerate(nomes):
        print(f'{indice +1} - {opcao}')

def cadastrar_nome(nome):
    nomes.append(nome)

def atualiza_nome(nome, novo_nome):
    nomes[nomes.index(nome)] = novo_nome

def exclui_nome(nome):
    nomes.remove(nome)
    