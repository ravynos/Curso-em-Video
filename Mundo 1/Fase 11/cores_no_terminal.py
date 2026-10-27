#Formatação de cores no terminal python com padrão ANCI

#   Style           Text                Back
#   0 = None        30 = Branco         40 = Branco
#   0 = Bold        31 = Vermelho       41 = Vermelho
#   0 = Underline   32 = Verde          42 = Verde
#   0 = Negative    33 = Amarelo        43 = Amarelo
#                   34 = Azul           44 = Azul
#                   35 = Magenta        45 = Magenta
#                   36 = Ciano          46 = Ciano
#                   37 = Cinza          47 = Cinza

# Letra branca, fundo vermelho
print('\033[0;30;41mTeste\033[m')

#Letra amarela, sublinhada com fundo azul
print('\033[4;33;44mTeste\033[m')

#Letra magenta. em negrito, fundo amarelo
print('\033[1;35;43mTeste\033[m')

#Fundo verde, letra banca
print('\033[0;30;42mTeste\033[m')

#Letra banca
print('\033[mTeste\033[m')

#Letra banca
print('\033[7mTeste\033[m')