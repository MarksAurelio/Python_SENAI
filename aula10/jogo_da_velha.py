def menu():
    continuar = 1
    while continuar:
        continuar = int(input('1. Novo jogo \n'+ '2. Finalizar \n'))
        if continuar == 1:
         game() 
        elif continuar == 2:
            print('Saindo') 
            break
        else:
            print('Opção inválida')
            
        
            

def game():
    jogada = 0

    while ganhou() == 0:
        print('\nJogador', jogada % 2 + 1)
        exibe()
        linhas  = int(input('\nEscolha uma linha : '))
        colunas = int(input('Escolha uma coluna: '))

        if bordas [linhas - 1][colunas - 1] == 0:
            if (jogada % 2 + 1) == 1:
                bordas [linhas-1][colunas-1] = 1
            else:
                bordas [linhas-1][colunas-1] = -1
        else:
            print('Não está vazio')
            jogada -= 1

        if ganhou():
            print('Jogador', jogada %2 + 1,'ganhou após', jogada + 1, 'rodadas')

        jogada += 1

def ganhou():
    # Conferindo as linhas
    for i in range(3):
        soma = bordas [i][0] + bordas [i][1] + bordas [i][2]
        if soma == 3 or soma == -3:
            return 1

     # Conferindo as colunas
    for i in range(3):
        soma = bordas [0][i] + bordas [1][i] + bordas [2][i]
        if soma == 3 or soma == -3:
            return 1

    # Conferindo as diagonais
    diagonal1 = bordas [0][0] + bordas [1][1] + bordas [2][2]
    diagonal2 = bordas [0][2] + bordas [1][1] + bordas [2][0]
    if diagonal1 == 3 or diagonal1 == -3 or diagonal2 == 3 or diagonal2 == -3:
        return 1

    return 0

def exibe():
    for i in range(3):
        for j in range(3):
            if bordas [i][j] == 0:
                print(" _ ", end=' ')
            elif bordas [i][j] == 1:
                print(" X ", end=' ')
            elif bordas [i][j] == -1:
                print(" O ", end=' ')

        print()
                

bordas = [ [0,0,0],
           [0,0,0],
           [0,0,0] ]

menu()