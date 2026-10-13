# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.

m = input('Digite algo, e descubra informações sobre ele.')

print(type(m))
print(m.isnumeric())
print(m.isalpha())
print(m.islower())