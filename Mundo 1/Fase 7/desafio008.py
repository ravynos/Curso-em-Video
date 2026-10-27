# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input('Quantos metros deseja converter? '))

cm = m * 100
mm = m * 1000

print(f"Em {m} metro, temos {cm} centrimetros e {mm} milimetros")