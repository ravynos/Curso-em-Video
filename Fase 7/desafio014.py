#Escreva um programa que converta uma tempratura digitada em °C e conferta para ° F.

celsius = float(input('Qual temperatura em °C deseja converter?: '))

fahrenheit = celsius * 9 / 5 + 32

print(f'{celsius}°C equivale a {fahrenheit}°F')