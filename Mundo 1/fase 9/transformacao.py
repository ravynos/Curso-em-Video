# Metoodos para transformação de uma lista de string.


frase = 'Curso em Vídeo Python'
frase_esp = '   Aprenda Python   '

print('Realizando a transformação de listas de string \n')

print(f'Substituindo frases em uma lista de string: {frase.replace('Python', 'Android')}')
# Substituindo frases em uma lista de string: Curso em Vídeo Android
print(f'Deixa todas as letras da frase em Maiusculo: {frase.upper()}')
# Deixa todas as letras da frase em Maiusculo: CURSO EM VÍDEO PYTHON
print(f'Todas as letras minutos: {frase.lower()}')
# Todas as letras minutos: curso em vídeo python
print(f'Capitalizar a frase, todas as letras ficam minusculas somente a 1° em maiusculo: {frase.capitalize()}')
# Capitalizar a frase, todas as letras ficam minusculas somente a 1° em maiusculo: Curso em vídeo python
print(f'Aplica o Capitalize em todas as palavras da frase: {frase.title()}')
# Aplica o Capitalize em todas as palavras da frase: Curso Em Vídeo Python
print(f'Funcionalidade para remover espaços inuteis: {frase_esp.strip()}')
# Funcionalidade para remover espaços inuteis: Aprenda Python
print(f'Retirando espaços a direita: {frase_esp.rstrip()}')
# Retirando espaços a direita:    Aprenda Python
print(f'Removendo espaços a esqueda: {frase_esp.lstrip()}.')
# Removendo espaços a esqueda: Aprenda Python  .
