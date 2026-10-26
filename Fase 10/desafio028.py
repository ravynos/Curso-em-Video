# Escreva um programa que faça o computador "Pensar" em um numero, inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

n = randint(0, 5)

n2 = int(input('Adivinhe um nomero de 0 a 5: '))

if n2 == n:
    print('Acerrtou!!!')
else: 
    print('Errou')