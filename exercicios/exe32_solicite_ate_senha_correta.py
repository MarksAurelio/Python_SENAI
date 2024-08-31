# 52. Desenvolva um algoritmo que solicite ao usuário uma senha 
# e continue pedindo até que a senha correta "1234" seja digitada.

senha_correta = '1234'
senha_digitada = ''

while senha_correta != senha_digitada:
    senha_digitada = input('Digite a possível senha: ')

print('A senha está correta!')