
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

### Operadores

- Aritméticos
- Atribuição
- Relacionais
- Lógicos
- Ternário

>Aritméticos

| Operador | Nome             |
| -------- | ---------------- |
| +        | Soma             |
| -        | Subtração        |
| *        | Multiplicação    |
| /        | Divisão          |
| %        | Resto da Divisão |
| **       | Exponenciação    |

**Ordem de Precedência**

A ordem segue a lista do primeiro ao ultimo.

| Operador   | Nome                                   |
| ---------- | -------------------------------------- |
| ( )        | Parentêses                             |
| **         | Exponenciação                          |
| *   /    % | Multiplicação/Divisão/Resto da Divisão |
| +   -      | Subtração                              |

>Atribuição

O símbolo de igual (=), para o JS, tem função de atribuição, podendo ser traduzido como "recebe".

```JavaScript
//Atribuição Simples
var a = 5+3            //5 + 3 = 8
var b = a % 5          //8 % 5 = 3
var c = 5 * b ** 2     //3 * 3 = 9 * 5 = 45
var d 10 - a / 2       //8 / 2 = 4 10 - 4 = 6
var e 6 * 2 / d        //6 * 2 = 12 / 6 = 2
var f = b % e + 4 / e  //3 % 2 = 1 4 / 2 = 2 1 + 2 = 3
```

**Auto-atribuições**

Posso reatribuir um valor a minha variável de acordo com o contexto que vou utilizar.

```JavaScript
var n = 3
n = n + 4   //7
n = n - 5   //2
n = n * 4   //8
n = n / 2   //4
n = n ** 2  //16
n = n % 5   //1

// Todas as atribuições acima fez que no final n tenha o valor 1.
n = 1
```

Simplicando

Se a variável esta recebendo ela e um novo valor e possível usar o operador = ao valor.

```JavaScript
n = n + 4 -->  n += 4
n = n - 5 -->  n -= 5
n = n * 4 -->  n *= 4
n = n / 2 -->  n /= 2
n = n ** 2 --> n ** 2
n = n % 5 -->  n % 5
```

Incremento

Para simplificar e possível usar o operador 2 vezes, e será entendido que e para fazer a operação com número 1.

