# Desenvolva um programa que leia o cumprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o tamanho do primeiro lado do triangulo: '))
b = float(input('Digite o tamanho do segundo lado do triangulo: '))
c = float(input('Digite o tamanho do terceiro lado do triangulo: '))

if a + b > c and a + c > b and b + c > a:
    print('Forma um triangulo')
else:
    print('Não forma um triangulo')