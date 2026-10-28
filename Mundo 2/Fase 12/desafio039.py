# Faça um programa que leia o ano de nascimento de um jovem, de acordo com sua idade:

# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo de alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nascimento = int(input('Qual o ano do seu nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade == 18:
    print('Está na hora de se alistar!')
elif idade < 18:
    print(f'Faltam {18 - idade} anos para se alistar')
elif idade > 18:
    print(f'Passou {idade - 18} anos do seu prazo de se alistar')