""" Desafio 011 """

"""Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo 
que cada litro de tinga, pinta uma área de 2m².

"""

altura = float(input("Qual a altura da parede? "))
largura = float(input("Qual a largura da parede? "))
area = altura * largura
tinta = area / 2

print(f"Em uma parede de {altura} m por {largura} m com área de {area} m² será necessário o total de {tinta} l de tinta para pintar toda a parede.")