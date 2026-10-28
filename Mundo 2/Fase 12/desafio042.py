# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# - Equilátero:  Todos os lados iguais
# - Isóceles: dois lados iguais
# - Escaleno: Todos os lados diferentes

a = float(input('Digite o tamanho do primeiro lado do triangulo: '))
b = float(input('Digite o tamanho do segundo lado do triangulo: '))
c = float(input('Digite o tamanho do terceiro lado do triangulo: '))

if a + b > c and a + c > b and b + c > a:
    print('Forma um triangulo')
    if a == b == c:
        print('Triâgulo Equilátero')
    elif a == b != c or a == c != b or b == c != a:
        print('Triângulo Isóceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Não forma um triangulo')