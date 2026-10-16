# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar.
#Considere US$1,00 = R$5,06

cat = float(input('Quanto você possui na carteira agora? '))

conv = cat / 5.06

print(f'Com {cat} reais, você pode comprar {conv:.2f}')