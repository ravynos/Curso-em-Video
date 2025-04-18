""" Desafio 004 """

""" Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
todas as informções possíveis sobre ele. """

char = input('Digite algo e veja o que aparece: ')
print(type(char))
print(f'O que você digitou e um numero? {char.isnumeric()}')
print(f'O que você digitou e são letras? {char.isalpha()}')