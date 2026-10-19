# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Qual o angulo a calcular?: '))
ang_conv = radians(angulo)

print(f'O ângulo de {angulo:.1f}°, converte em {ang_conv:.2f} para radianos, e possui seno {sin(ang_conv):.2f}, cosseno {cos(ang_conv):.2f} e tangente{tan(ang_conv):.2f} ')