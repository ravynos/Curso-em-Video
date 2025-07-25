""" Desafio 015 """

"""Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

quantos_km = float(input("Quantos KM rodou? "))
quantos_dias = float(input("Quantos dias? "))
valor_dia = 60
valor_km = 0.15

calculo_dias = quantos_dias * valor_dia
calculo_km = quantos_km * valor_km

valor_total = calculo_dias + calculo_km

print(f"Seu carro ficou alugado por {quantos_dias} dias, e percorreu {quantos_km} km durante o periodo do aluguel, o valor total do aluguel ficou em R${valor_total}.")