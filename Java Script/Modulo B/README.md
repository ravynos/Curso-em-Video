
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

Exemplos
```JavaScript
x = x + 1 x ++
x = x - 1 x --
```

> Relacionais

| Operador | Nome           |
| -------- | -------------- |
| >        | Maior          |
| <        | Menor          |
| >=       | Maior ou igual |
| <=       | Menor ou igual |
| ==       | Igual          |
| !=       | Diferente      |

```JavaScript
5 > 2 --> true
7 < 4 --> false
8 >= 8 --> true
9 <= 7 --> false
5 == 5 --> true
4 != 4 --> false
```

Exemplos

``` JS
preco >= 200.50             // o preço é maior ou igual a 200.5?
idade < 18                  // a idade é menor do que 18?
curso == 'JavaScript'       // o curso é JavaScript?
n1 != n2                    //n1 é diferente de n2?
``` 

**Identidade**

Ao fazer a comparação com de 2 valores, o JS não testa o tipo, somente o valor, conforme exemplo abaixo:

```JS
5 == 5 --> true
5 == '5' --> true
5 === '5' --> false 
5 === 5 --> true
```

No caso acima, quando testarmos 5 == 5, o JS entende como verdadeiro, quando testamos 5 == '5', o JS também entende como verdadeiro, porque o conteúdo e o mesmo, ele não verifica se o segundo numero e uma string.

Para esse teste usamos o operador de igualdade restrita, esse sim, testa além do valor o seu tipo, 5 === '5' assim ele vai responder como falso, pois os valores são iguais, mas o tipo não, e caso realizamos o teste de 5 === 5, ele vai dar o resultado verdadeira, porque os 2 são idênticos em valor e tipo.

> Lógicos

| Operador | Nome           |
| -------- | -------------- |
| !        | Negação        |
| &&       | Conjunção (e)  |
| \|\|     | Disjunção (ou) |
Conforme exemplo abaixo, o operador de negação tem somente um operando, ele que dizer não, basicamente ele inverte o resultado, negando o resultado atribuído a ele.

```JS
! true --> false
! false --> true
```

Conforme exemplo abaixo, esse operador && um operador binário, ele precisa de 2 valores para operar. Nesse caso o operador somente vai dar o resultado verdadeiro, se os 2 valores forem verdadeira, em qualquer outra condição ele e falso.

```JS
true && true --> true
true && false --> false
false && true --> false
false && false --> false
```

Já no próximo exemplo, vamos exemplificar o operador || que retornará resultado verdadeiro se qualquer uma das condições sejam verdadeiras.

```JS
true || true --> true
true || false --> true
false || true --> true
false || false --> false
```



Exemplos

```JS
idade >= 15 && idade <= 17       // a idade esta entre 15 e 17?
estado == 'RJ' || estado =='SP'  // o estado é RJ ou SP?
salário > 1500 && sexo != 'M'    //o salário é acima de 1500 e não é homem?
```

Ordem de precedência entre operadores:

Aritméticos: Seguindo sua ordem de precedência normalmente
Atribuição: Não a ordem de precedência entre eles, sendo resolvido o que aparece primeiro.
Lógicos: Seguindo a seguinte ordem ! --> && --> ||

> Ternário

teste ? true : false

Após a realização de um teste lógico, podemos definir o resultado caso seja verdadeiro ou falso.

Exemplo:

```JS
media >= 7.0 ? "Aprovador" : "Reprovado"
media = 8.0 --> "Aprovado"
media = 5.5 --> "Reprovador"
```

