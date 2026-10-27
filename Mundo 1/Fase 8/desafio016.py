# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua poção inteira.

# Ex: Digite um número 6127 - O Número 6127 tem a parte inteira 6.

from math import trunc

n = float(input('Qual numero você deseja saber sua parte inteira?: '))

print(f'A parte inteira de {n} é {trunc(n)}')