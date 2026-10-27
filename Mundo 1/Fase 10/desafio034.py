# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para saláfrios superiores a R$1250,00, calcule um aumento de 10%.

#Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual salario do funcionario?: '))

if salario > 1250:
    aumento = (10 * salario) / 100
else:
    aumento = (15 * salario) / 100

salario += aumento

print(f'O novo salario do funcionario é R$ {salario}')