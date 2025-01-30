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