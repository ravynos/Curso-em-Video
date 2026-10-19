# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

al1 = input('Informe o nome do aluno: ')
al2 = input('Informe o nome do aluno: ')
al3 = input('Informe o nome do aluno: ')
al4 = input('Informe o nome do aluno: ')

alunos = [al1, al2, al3, al4]

print(f'O aluno escolhido para apagar o quadro é {choice(alunos)}')