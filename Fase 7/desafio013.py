# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

salario = float(input('Qual o salário do funcionário?: '))
aumento = salario * 15 / 100

print(f'Esse funcionário passa a receber {salario + aumento} ao aplicar 15% de aumento.')