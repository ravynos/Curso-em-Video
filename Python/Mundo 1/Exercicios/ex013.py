""" Desafio 013 """

"""Faça um algoritmo que leia o salário de um funcionário e mostre seu novo
salário, com 15% de aumento."""

salario = float(input("Qual o salário do funcionário? "))
calculo_aumento = salario * 0.15
novo_salario = salario + calculo_aumento

print(f"O salário do funcionário e {salario}, o seu aumento de 15% deve ser de {calculo_aumento}, seu novo salário é de {novo_salario}")