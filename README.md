# Gerador de resumos

Criado na linguagem Python utilizando o framework para desenvolvimento web [Flask](https://flask.palletsprojects.com/en/3.0.x/), a [Api da Google Gemini](https://ai.google.dev/gemini-api?hl=pt-br) e a biblioteca [Bootstrap](https://getbootstrap.com/).

## Como funciona

Utiliza a IA generativa Gemini pra dividir um texto num formato específico (que é demonstrado para a IA no momento em que é realizado o prompt através de alguns exemplos), separando-o em:

* Tema principal
* Tópicos abordados
* Resumo 

Possuindo a possibilidade de gerar o resultado em vários idiomas, além de escolher o grau de formalidade da resposta (que ao ser escolhido, altera o parâmetro de "temperatura" da IA, influenciando assim na escolha das palavras).

## Exemplos de uso
* Traduções de texto
* Dividir em tópicos textos muito grandes
* Resumir textos com menor formalidade para facilitar o entendimento

