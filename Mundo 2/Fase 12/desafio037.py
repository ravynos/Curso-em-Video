# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.

# -1 para binário
# -2 para octa
# -3 para hexadecimal

numero = int(input('Qual número deseja converter? '))
opção = int(input('Qual base númerica deseja converter?\n1 - Binário\n2 - Octa\n3 - Hexadecimal\nDigite: '))

if opção == 1:
    print(f'O valor digitado em binário é \033[1;32m{numero:b}\033[m')
elif opção == 2:
    print(f'O valor digitado em Octa é \033[1;33m{numero:o}\033[m')
elif opção == 3:
    print(f'O valor digitado em Hexadecimal é \033[1;34m{numero:x}\033[m')
else:
    print('\033[1;30;41mOpção invalida!\033[m')