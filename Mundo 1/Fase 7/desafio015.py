# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias_aluguel = int(input('Quantos dias alugados?: '))
km_percorridos = float(input('Quantos KM esse carro percorreu?: '))

total_aluguel = 60 * dias_aluguel
total_km = 0.15 * km_percorridos

print(f'Esse carro foi alugado por: {dias_aluguel} dias\nPercorrendo: {km_percorridos} Kms\nTotal de R${total_aluguel:.1f} pelos dias alugados\nTotal de R$ {total_km} pelo percurso efetuado')
print(f'Total a pagar {total_km + total_aluguel}')