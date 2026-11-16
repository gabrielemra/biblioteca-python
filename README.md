# Sistema de Gerenciamento de Biblioteca

Programa simples em Python, feito para rodar no terminal, que gerencia o acervo de uma biblioteca. Ele guarda o título e o autor de cada livro, mostra quais estão disponíveis ou emprestados e registra para quem cada livro foi emprestado.

## Funcionalidades

- **Cadastrar livro:** com código, título e autor. O código não pode se repetir, e título e autor não podem ficar vazios.
- **Listar livros:** mostra todos os livros com o status de cada um (disponível ou emprestado para quem).
- **Emprestar livro:** registra o nome de quem pegou o livro.
- **Devolver livro:** o livro volta a ficar disponível.
- **Salvamento automático:** os livros ficam guardados em arquivo, então não se perdem quando o programa é fechado.

## Como executar

É preciso ter o Python 3 instalado. O programa usa só bibliotecas que já vêm com o Python, então não precisa instalar mais nada.

```bash
python biblioteca.py
```

## Como os dados são guardados

Os livros são salvos no arquivo `biblioteca.json`, que é criado sozinho na pasta do programa. Ele é gravado a cada cadastro, empréstimo ou devolução (função `salvar_livros`, com `json.dump`) e lido quando o programa abre (função `carregar_livros`, com `json.load`).

## O que aprendi

Precisei rodar o código várias vezes para perceber que faltavam alguns acabamentos. Dois exemplos:

- `ensure_ascii=False`, para o arquivo guardar as letras com acento do jeito que são, sem trocá-las por códigos.
- `.strip()`, para não aceitar campos vazios ou só com espaços, o que deixaria cadastrar um livro com título em branco.

## Observações

- O código do livro é guardado como número, então `001` é salvo como `1`.

## Autora

Gabriele Moreira Pereira

- LinkedIn: [linkedin.com/in/gabrielemoreirapereira](https://www.linkedin.com/in/gabrielemoreirapereira)
- GitHub: [gabrielemra](https://github.com/gabrielemra)
