""" Desafio 012 """

"""Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto."""

preco = float(input("Qual o valor do produto? "))
desconto = preco * 0.05
final = preco - desconto

print(f"O valor do seu produto é {preco}, com o desconto de 5% fica o valor de {final}")