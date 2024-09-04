# 53. Escreva um programa que peça ao usuário um número 
# e exiba a contagem regressiva desse número até 1.

from os import system
import time # para contagem regressiva

numero = int(input('Informe o número: '))

while numero >= 1:
    system('Clear') # limpar o terminal
    print(numero)
    numero -= 1 # regressiva
    time.sleep(1) # sleep de tempo regressivo de (time)
