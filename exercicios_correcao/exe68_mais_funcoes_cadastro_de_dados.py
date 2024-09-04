# 68. Crie uma nova versão do algoritmo 66, aplicando o conceito de módulos e dividindo as responsabilidades,
#  receberemos agora não somente o nome, mas simularemos um sistema de cadastro de alunos, 
# esta nova versão deve atender as novas funcionalidade a seguir:
# Cada aluno cadastrado deve ter atrelado a seus dados pessoais (nome, e-mail, data de nascimento, matricula), 
# no caso de matricula você deve gerar uma matricula unica para cada aluno cadastrado.
# Cada um dos dados do aluno devem ser validade de forma o código não quebre ao serem informados valores incorretos.
# Para atualizar qualquer dado do aluno você deve localiza-lo utilizando de sua matricula para isso. 
# Valide de forma que o sistema não quebre ao ser inserido uma matricula invalida.
# Para remover um aluno deve-se realizar esta ação usando de sua matricula, o sistema não pode quebrar ao ser inserido uma matricula errada.
# Ao listar todos os alunos mostre cada um de forma organizada e separada.
# Crie uma funcionalidade de mostre os dados de um aluno especifico usando apenas de sua matricula para isso.

operacao = 'sim'

while operacao == 'sim':
    op.menu()
    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
            nome = input('que nome deseja cadastrar? ')
            op.cadastrar_nome(nome)
        case 2:
            nome = input('Que nome deseja atualizar? ')
            novo_nome = input('Qual será o novo nome: ')

            op.atualiza_nome(nome, novo_nome)

        case 3:
            nome = input('Que nome deseja remover? ')
            op.exclui_nome(nome)
        case 4:
            op.listar_nomes()
        case _:
            print('opção inválida')

    operacao = input('Deseja realizar outra operação? ').lower()
    system('clear')

    if operacao != 'sim':
         break