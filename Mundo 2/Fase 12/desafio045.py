# Crie um programa que faça o computador jogar Jokenpô com você

from random import choice

escolha = int(input('Escolha:\n1 - Pedra\n2 - Papel\n3 - Tesoura\nEscolha: '))

opcoes = ['Pedra', 'Papel', 'Tesoura']

sorteio = choice(opcoes)


if escolha == 1:
    escolha = 'Pedra'
elif escolha == 2:
    escolha = 'Papel'
elif escolha == 3:
    escolha = 'Tesoura'
#else:
#    print('Invalido')

if escolha in opcoes:
    if escolha == 'Pedra' and sorteio == 'Tesoura':
        print('Você Venceu')
    elif escolha == 'Pedra' and sorteio == 'Papel':
        print('Você Perdeu')
    elif escolha == 'Papel' and sorteio == 'Pedra':
        print('Você Venceu')
    elif escolha == 'Papel' and sorteio == 'Tesoura':
        print('Você Perdeu')
    elif escolha == 'Tesoura' and sorteio == 'Papel':
        print('Você Venceu')
    elif escolha == 'Tesoura' and sorteio == 'Pedra':
        print('Você Perdeu')
    elif escolha == sorteio:
        print('Empate')
    print(sorteio)
else:
    print('Escolha invalida')