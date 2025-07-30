""" Desafio 019 """

"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido."""

import random

aluno1 = input("Qual o nome do 1° aluno? ")
aluno2 = input("Qual o nome do 2° aluno? ")
aluno3 = input("Qual o nome do 3° aluno? ")
aluno4 = input("Qual o nome do 4° aluno? ")

numero_sorteado = random.randint(1, 4)

aluno_sorteado = ""
if numero_sorteado == 1:
    aluno_sorteado = aluno1
elif numero_sorteado == 2:
    aluno_sorteado = aluno2
elif numero_sorteado == 3:
    aluno_sorteado = aluno3
else:
    aluno_sorteado = aluno4

print("\nSorteando")
print(f"O aluno sorteado foi: {aluno_sorteado}")