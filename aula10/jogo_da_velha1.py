import jogo_da_velha_funcoes as jvf

jogador = 'X'
vencedor = False

while vencedor == False:

    jvf.desenhar_tabuleiro()

    jogada = int(input('Onde deseja jogar? '))

    jvf.jogar(jogada, jogador)

    jvf.desenhar_tabuleiro()

    jogador = jvf.verifica_vitoria(jogador)
    vencedor = jvf.troca_jogador()

jogador = jvf.troca_jogador(jogador)
print(f'O jogador "{jogador}" venceu')