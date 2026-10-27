# Faça um programa que leia o preço de um produto e o percentual de desconto desejado.
# Calcule e mostre o valor do desconto e o preço final do produto após a aplicação desse desconto.

preco = float(input('Qual o valor do produto sem desconto?: '))
des = float(input('Qual valor do desconto?: '))
cdes = preco * des / 100

print(f'Seu produto com desconto de {des}% custa {preco - cdes}')