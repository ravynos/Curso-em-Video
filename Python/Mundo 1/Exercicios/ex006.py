""" Desafio 006 """

""" Crie um algoritimo que leia um número e mostre seu dobro, seu triplo e
raiz quadrada. """

import math

numero = float(input("Qual numero vocÊ deseja saber seu dobro, triplo é sua raiz quadarada?"))
dobro = numero * 2
triplo = numero * 3
raiz = math.sqrt(numero)

print(f"O dobro de {numero} é {dobro}. \nO triplo é {triplo}. \nA raiz quadrada é {raiz:.2f}")