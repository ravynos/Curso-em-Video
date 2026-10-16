# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta 
# uma área de 2m².

lar = float(input('Digite a largura de sua parede: '))
alt = float(input('Digite a altura da sua parede: '))

area = lar * alt

print(f'Sua parede tem {area} m², e você precisa de {area / 2} litros para pintar sua parede.')