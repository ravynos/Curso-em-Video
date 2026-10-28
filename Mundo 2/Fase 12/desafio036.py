# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado.

valor_casa = float(input('Qual o valor da casa a ser comprada? '))
salario = float(input('Qual salário do comprado? '))
anos_pagamento = float(input('Em quantos anos pretente pagar? '))

prest_anos = anos_pagamento * 12
valor_prestacao = valor_casa / prest_anos
porc_salario = salario * 0.30

if valor_prestacao > porc_salario:
    print(f'Emprestimo Recusado, valor da prestação é {valor_prestacao:.2f} exede 30% do salario')
else:
    print(f'Emprestimo aprovado, valor das prestações {valor_prestacao:.2f}')