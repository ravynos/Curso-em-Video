# Faça um programa que leia um ano qualquer e mostre se ele e BISSEXTO.

ano = int(input('Qual ano deseja saber se e bissexto?: '))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print(f'{ano} e um ano BISSEXTO')
else:
    print(f'{ano} não e um ano BISSEXTO')