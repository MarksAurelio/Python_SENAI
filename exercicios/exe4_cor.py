# 4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.

vermelho = 'vermelho'
verde = 'verde'
azul = 'azul'

cores = str(input('Digite uma cor vermelho, verde ou azul? '))
if cores == vermelho:
    print('vermelho')
if cores == verde:
    print('verde')
if cores == azul:
    print('azul')
else:
    print('Essa cor não faz parte da relação apresentada')
    

