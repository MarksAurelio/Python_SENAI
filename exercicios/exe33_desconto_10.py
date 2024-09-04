# 33. Crie um programa que solicite ao usuário o valor de um produto 
# e calcule o desconto de 10%.

valorProduto = float(input('Digite o valor do produto: \n'))
desconto = valorProduto * 0.1
valorDesconto = valorProduto - desconto

print('O valor do produto com 10% é', valorDesconto)
