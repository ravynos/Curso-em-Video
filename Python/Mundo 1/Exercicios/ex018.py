""" Desafio 018 """

"""Faça um programa que leia um ãngulo qualquer e mostre na tela o valor do
seno, cosseno e tangente desse ãngulo."""

from math import cos, sin, tan, radians

angulo_graus = float(input('Digite o ãngulo em graus: '))
angulo_radianos = radians(angulo_graus)
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

print(f'Para o ângulo de {angulo_graus}°:')
print(f'O Seno é: {seno:.2f}')
print(f'O Cosseno é: {cosseno:.2f}')
print(f'A tangente é: {tangente:.2f}')