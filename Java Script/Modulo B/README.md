
# Modulo B

## Comentários

// =  Comenta a linha que ela se encontra
\/*  Código * / = Comenta um bloco inteiro no documento.


## Variáveis

### Identificadores

- Podem começar com letras, $ ou _
- Não podem começar com números
- É possível usar letras ou números
- É possível usar acentos e símbolos
- Não pode conter espaços
- Não podem ser palavras reservadas

>Dicas

- Maiúsculas e minúsculas fazem diferença
- Tente escolher nomes coerentes para as variáveis
- Evite se tornar um 'programador alfabeto' ou um 'programador contador'

### Tipos de dados

>Tipo Primitivos

- Number
	- Infinity
	- NaN
- String
- Boolean
- Null
- Undefined
- Object
	- Array
- Function

>Conversão de tipos

String --> Número

Number.parseInt(n): Converte o valor de uma variável de string para inteiro.
Number.parseFloat(n): Converte o valor de uma variável de string para Real.
Number(n): O próprio JS decide de acordo com o valor digitado qual o tipo de dado.

Número  --> String

String(n):
n.toString()

> Formatando Strings

```JavaScript
var s = 'JavaScript'
'Eu estou aprendendo s' //não faz interpolação
'Eu estou aprendendo' + s //Usa concatenaçaõ
`Eu estou aprendendo ${s}` //usa template string
s.length // Quantos caracteres a string possui
s.toUpperCase() //tudo para 'MAIÚSCULAS'
s.toLowerCase() //tudo para 'minúsculas'
```

Para usar o template string, e necessário usar a crase  ( \` \`) no lugar de aspas ("" ou ''), e ao declarar a variável, usaremos os placeholders ${} inserindo a variável dentro das chaves.

>Formatação de números

.toFixed(): Pode ser usado para definir a quatidade de casas decimais após a virgula.
.replace(): Pode substituir um símbolo por outro.
.toLocaleString(): Permite localizar um número de acordo com uma moeda.

```JavaScript
n1 = 1545.5
n1.toFixed(2)
'1545.50'

n1.toFixed(2).replace('.', ',')
'1545,50'

n1.toLocaleString('pt-BR', {style: 'currency', currency: 'BRL'})
'R$ 1,545,50'
```

