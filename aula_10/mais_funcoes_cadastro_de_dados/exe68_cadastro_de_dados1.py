from os import system
import mais_funcoes_operacoes as mop
# from operacoes import menu, listar_nomes
# import operações

operacao = 'sim'
matricula = 0

while operacao == 'sim':
    mop.menu()
    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
            nome = input('que nome deseja cadastrar? ')
            email = input('Qual é o email do aluno: ')
            data_nascimento = input('Informe a data de nascimento: ')

            matricula += 1
            op.cadastrar_nome(nome, email, data_nascimento, matricula)
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




