""" Desafio 007 """

""" Desenvolva um programa que leia as duas notas de um aluno é calcule a sua média."""

nota1 = float(input("Qual a nota do primeiro semestre do Aluno? "))
nota2 = float(input("Qual a nota do segundo semestre do Aluno? "))
media = (nota1 + nota2) / 2

print(f"Esse aluno teve Nota: {nota1} no primeiro semestre, Nota: {nota2} no segundo semestre e sua média é {media:.1f}.")
