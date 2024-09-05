from os import system
import operacoes as op
# from operacoes import menu, listar_nomes
# import operações

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




