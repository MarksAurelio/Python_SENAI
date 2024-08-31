# 57. Crie um programa que peça ao usuário para adivinhar um número secreto entre 1 e 10. 
# Continue pedindo até que ele adivinhe o número corretamente.
import random
numeroSecreto = random.randint(1, 10)
numeroSecreto = 3
tentativas = 0

while True:
    chute = int(input('Adivinhe um número entre 1 a 10? \n'))
    tentativas += 1

    if chute < numeroSecreto or chute > numeroSecreto:
        print('Ainda não é o número')
    else:
      print(f"Parabéns! Você acertou em {tentativas} tentativa(s).")
    