# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# - Até 9 anos: MIRIN
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 30 anos: SÊNIOR
# - Acima: MASTER

from datetime import date

ano_nascimento = int(input('Qual seu ano de nascimento? '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Categoria: MIRIN')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 30:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')