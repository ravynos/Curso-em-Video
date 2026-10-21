# Faça um programa que leia uma frase pelo telcado e mostre:

# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = input('Digite uma frase: ')

print(frase.upper().count('A'))

print(frase.lower().find('a'))

print(frase.lower().rfind('a'))