""" Desafio 014 """

"""Escreva um programa que converta uma temperatura digitando 
em graus Celsius e converta para graus Fahrenheit."""

temperatura = float(input("Qual a temperadura deseja converter? "))
calculo_f = temperatura * 1.8 + 32

print(f"A temperadura de {temperatura}°C convertida em Fahrenheit é {calculo_f}°F")