# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt, hypot

cat_op = float(input('Qual o valor do cateto oposto?: '))
cat_ad = float(input('Qual o valor do cateto adjacente?: '))

elev_quad = (cat_op ** 2 + cat_ad ** 2)

print(f'O valor do comprimento da hipotenusa é {sqrt(elev_quad)}')
print(hypot(cat_op, cat_ad))