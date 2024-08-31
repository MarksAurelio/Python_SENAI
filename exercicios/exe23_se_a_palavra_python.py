# 23. Crie um algoritmo que peça ao usuário uma palavra e verifique se a palavra é "Python"

palavra = input('Digite uma palavra: \n')
palavra = palavra.lower()

if palavra == "python":
    print('Você digitou a palavra Python')
else:
    print('Você não digitou a palavra Python')