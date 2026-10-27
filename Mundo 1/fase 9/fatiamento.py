frase = 'Curso em Vídeo Python'

print('Esse exercicio se trata do fatiamente de string: \n')

print(f'Buscando um unico indice: {frase[9]}')
# Buscando um unico indice: V
print(f'Buscando uma faixa (exibe sempre entre o indice inicial até o anterior ao declarado): {frase[9:13]}')
# Buscando uma faixa (exibe sempre entre o indice inicial até o anterior ao declarado): Víde
print(f'Buscando até o ultimo caracter da frase: {frase[9:21]}')
# Buscando até o ultimo caracter da frase: Vídeo Python
print(f'Buscando uam faixa, e pulando de 2 em 2: {frase[9:21:2]}')
# Buscando uam faixa, e pulando de 2 em 2: VdoPto
print(f'Buscando uma faixa iniciando com indice 0: {frase[:5]}')
# Buscando uma faixa iniciando com indice 0:Curso
print(f'Buscando até o final da string, quando vc não sabe qual é: {frase[15:]}')
# Buscando até o final da string, quando vc não sabe qual é: Python
print(f'Mesmo caso do anterior, porém pulando de 3 em 3: {frase[9::3]}','\n')
# Mesmo caso do anterior, porém pulando de 3 em 3: VePh

print('\nUsando funções: \n')
print(f'Exibe a quantidade de caracter na frase/variavel: {len(frase)}')
# Exibe a quantidade de caracter na frase/variavel: 21
print(f'Contando quantas vezes aparece um determinado caracter: {frase.count('o')}')
# Contando quantas vezes aparece um determinado caracter: 3
print(f'Contagem com fatiamento: {frase.count('o', 0, 13)}')
# Contagem com fatiamento: 1
print(f'Encontrando frases e/ou letras na string, mostrando em que ponto ela começa: {frase.find('deo')}')
# Encontrando frases e/ou letras na string: 11
print(f'Usando find com string não presente na frase: {frase.find('Android')}')
# Usando find com string não presente na frase: -1
print(f'Procurando se uma palavra existe na frase usando o operador in: {'Curso' in frase}')
# Procurando se uma palavra existe na frase usando o operador in: True

