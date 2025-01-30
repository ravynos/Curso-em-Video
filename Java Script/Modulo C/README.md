# Modulo C - Entendendo o DOM

## Introdução ao DOM

> O que é DOM?

DOM --> **D**ocument **O**bject ***M*odel (Modelo de objetos para documentos)

Conjunto de objetos do seu navegador que da acesso aos componentes internos do seu website.

> Arvore DOM

window: A arvore dom começa pelo objeto window, tudo dentro do JD esta dentro do objeto window, dentro dele, existe vários outros objetos, alguns deles são:

- location: Onde e guardado o local do seu site, como URL, pagina atual, pagina anterior.
- document: Documento atual
	- html
		- head: Cabeçario
			- meta
			- title
		- body: Corpo
			- h1
			- p
				- strong
			- div
- history: Guarda o histórico de navegação.


> Selecionando Objeto

E possível acessar um objeto de varias formas, entre elas são:

- por Marca
	getEementsByTagName()
- por ID
	getEementByid()
- por Nome
	getEementsByName()
- por Classe
	getEementsByClassName()
- por Seletor
	querySelector()
	querySelectorAll()

## Eventos DOM

São eventos que acontecem durante qualquer interação do usuário com o site.

Por exemplo, uma \<div>, com o movimento do mouse, dentro de um elemento de uma div, pode disparar diversos eventos.

Alguns desses eventos:

mouseenter: Evento de entrada do mouse dentro do objeto.
mousemove: Evento de movimentar o mouse dentro da objeto.
mousedown: Evento de clicar no mouse e segurar.
mouseup: Evento de soltar o botão do mouse.
click: Evento de clicar no mouse.
mouseout: Evento de saída do mouse do objeto.

Para uma listagem completa dos eventos acesse: (https://developer.mozilla.org/en-US/docs/Web/Events)

> Funções

```JS
function ação(parametro){
bloco
}
```

