# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o útimo nome separadamente.

# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

nome = input('Digite seu nome completo: ')

nome = nome.split()

print(f'''Primeiro nome: {nome[0]}
Ultimo: {nome[-1]}''')