# Modulo D - Condições em JavaScript



## Condições em JS

if (se): Caso a condição imposta for verdadeira, o bloco de código ligado a ele e executado.
else(senão): Caso a condição de if seja falsa, o bloco ligado a ele e executado.

```JS
if (condição) {
bloco
}else {
bloco
}
```


>Tipo de condições

Condição Simples: é definido somente o if, caso a condição seja falsa, nada acontece.

```JS
if (condição){
bloco
}
```

Condição composta: E usado if e else, quando um não for atendido, o outro e executado.

```JS
if (condição) {
bloco
}else {
bloco
}
```

Condições aninhadas: São estruturas onde pode se definir condições dentro de outras condições.

```JS
if (cond1){
	bloco1
} else {
	if (cond2){
		bloco2
	} else {
		bloco3	
	}
}
```

> Buscando hora do sistema

Crie uma variável com o comando new Date(), ela pode ter qualquer nome, e outra variável chamado seu conteúdo, getHours() nesse caso, busca a hora.

```JS
var agora = new Date()
var hora =  agora.getHours()
var minuto = agora.getMinutes()

console.log(`Agora são exatamento ${hora}:${minuto} horas`)
if (hora< 12) {
    console.log('Bom dia!!!')
} else if (hora <= 18) {
    console.log('Boa tarde!!!')
} else {
    console.log('Boa noite!!!')
}
```

> Condição Múltipla


A estrutura switch permite verificar múltiplas condições de forma organizada. É útil quando se tem uma variável com muitos valores diferentes e se quer executar diferentes blocos de código.

```js
switch (expressão){
	case valor 1:
		bloco1
		break
	case valor 2:
		bloco2
		break
	case valor 3:
		bloco3
		break
	default:
		bloco4
		break
}
```

>[!Alert]
>Comando break e obrigatório abaixo de cada bloco, caso contrário, mesmo que a condição seja atendida, o teste continuará a ser feito em cada bloco case.

