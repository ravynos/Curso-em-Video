from math import sqrt, floor
import random
import emoji

num = int(input('Digite um número e saiba sua raiz quadrada. '))
raiz = sqrt(num)
print(f'A raiz quadrada de {num} é {floor(raiz)}')

num = random.randint(1, 10)
print(num)