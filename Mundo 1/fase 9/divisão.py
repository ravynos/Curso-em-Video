# Realizando a divisão em uma lista de strings.

frase = 'Curso em Vídeo Python'

print(f'Divide uma frase em uma lista: {frase.split()}')
# Divide uma frase em uma lista: ['Curso', 'em', 'Vídeo', 'Python']

# Juntando frases

print('Junção:\n')
frase = frase.split()

print(f'Juntando a lista e inserindo um separador: {'-'.join(frase)}')
# Juntando a lista e inserindo um separador: Curso-em-Vídeo-Python