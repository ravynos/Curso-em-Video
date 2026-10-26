# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
n3 = float(input('Digite o terceiro numero: '))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print(f'O maior numero digitado é {maior} o menor é {menor}')
    