# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com nome "Santo".

cidade = input('Qual nome da sua cidade:? ')

print(cidade.lower()[:5] == 'santo')