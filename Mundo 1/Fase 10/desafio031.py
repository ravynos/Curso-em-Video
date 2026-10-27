# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais
#longas.

km_rod = float(input('Quantos KM é a viagem?: '))

if km_rod <= 200:
    valor = km_rod * 0.50
    print(f'Sua viagem custará R${valor}')
else: 
    valor = km_rod * 0.45
    print(f'Sua viagem custará R${valor}')