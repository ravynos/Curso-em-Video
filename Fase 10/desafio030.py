# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um numero: '))

cal = num % 2

if cal == 0:
    print('Par')
else:
    print('Impar')