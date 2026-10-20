# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# EX: Digite um número 1834

# Unidade: 4
# Dezena 3
# Centena: 8
# Milhar: 1

numero = input('Digite um numero de 0 a 9999: ')
numero = numero.zfill(4)

print('Unidade: ', numero[3])
print('Dezena: ', numero[2])
print('Centena: ', numero[1])
print('Milhar: ', numero[0])