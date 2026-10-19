# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

al1 = input('Informe o nome do aluno: ')
al2 = input('Informe o nome do aluno: ')
al3 = input('Informe o nome do aluno: ')
al4 = input('Informe o nome do aluno: ')

alunos = [al1, al2, al3, al4]
shuffle(alunos)

print(f'1 - {alunos[0]}')
print(f'2 - {alunos[1]}')
print(f'3 - {alunos[2]}')
print(f'4 - {alunos[3]}')