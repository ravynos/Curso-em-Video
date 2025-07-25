""" Desafio 010 """

"""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode comprar

Considere US$1,00 = R$3,27

"""
carteira = float(input("Quanto você tem em sua carteira agora? "))
dolar = 3.27

print(f"O valor que você tem na carteira agora, e possível comprar US${carteira / dolar:.4}")