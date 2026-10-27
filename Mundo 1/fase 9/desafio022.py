# Crie um programa que leia o nome completo de uma pessoa e mostre:

# O nome com todas as letras maiúsculas
# O nome com todas minusculas.
# Quantas letras ao todo (Sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input('Qual seu nome completo?: ')

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
print(len(nome.split()[0]))