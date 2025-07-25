""" Desafio 016 """

"""Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex.: Digite um número: 6.127 O número 6.127 tem parte inteira 6."""

from math import trunc

num = float(input("Qual numero você deseja saber seu inteiro? "))
inteiro = trunc(num)

print(f'O inteiro de {num} é {inteiro}')