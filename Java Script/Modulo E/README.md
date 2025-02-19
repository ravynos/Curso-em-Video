# Modulo E -  Repetições

## Laços

### While (Enquanto)

	No laço de repetição while, enquando uma condição for verdadeira, vai ser repetido o bloco de código.

Exemplo:
```JS
// No exemplo abaixo, vou mostar uma função, que tem como objetivo, comer inteira uma pizza de 8 fatias.
function comerPizza(){
	comerfatia()
	comerfatia()
	comerfatia()
	comerfatia()
	comerfatia()
	comerfatia()
	comerfatia()
	comerfatia()
}

// Nesse exemplo, no exemplo acima, ele só vai funcionar, quando a pizza tiver 8 fatias, se ouver mais ela já não atenderia.

function comerPizza(){
	while(temFatia()){
	comerFatia()
	}
}
```

### DO (faça)

	Permite usar o laço while, mais com o teste logico acontecendo somente no final do bloco.

Exemplo: 
```JS
do {
	bloco
} while (condição)
```