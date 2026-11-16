import json
import os

ARQUIVO_DADOS = "biblioteca.json"


def salvar_livros(livros):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, indent=4, ensure_ascii=False)


def carregar_livros():
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto != "":
            return texto
        print("Este campo não pode ficar vazio!")


def buscar_livro(livros, codigo):
    for livro in livros:
        if livro["codigo"] == codigo:
            return livro
    return None


def cadastrar_livro(livros):
    codigo = ler_inteiro("Digite o código do livro: ")
    while buscar_livro(livros, codigo) is not None:
        print("Esse código já existe!")
        codigo = ler_inteiro("Digite outro código: ")

    titulo = ler_texto("Digite o título do livro: ")
    autor = ler_texto("Digite o autor do livro: ")

    livro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "disponivel": True,
        "emprestado_para": None
    }

    livros.append(livro)
    print("Livro cadastrado com sucesso!\n")


def listar_livros(livros):
    if len(livros) == 0:
        print("Nenhum livro cadastrado na biblioteca.\n")
    else:
        for livro in livros:
            if livro["disponivel"]:
                status = "Disponível"
            else:
                status = f"Emprestado para {livro.get('emprestado_para')}"
            print(f"Código: {livro['codigo']} | Título: {livro['titulo']} | Autor: {livro['autor']} | Status: {status}")
        print()


def emprestar_livro(livros):
    codigo = ler_inteiro("Digite o código do livro que deseja emprestar: ")
    livro = buscar_livro(livros, codigo)

    if livro is None:
        print("Livro não encontrado.\n")
    elif not livro["disponivel"]:
        print("Este livro já está emprestado.\n")
    else:
        nome_pessoa = ler_texto("Digite o nome de quem vai pegar o livro: ")
        livro["emprestado_para"] = nome_pessoa
        livro["disponivel"] = False
        print(f"O livro '{livro['titulo']}' foi emprestado para {nome_pessoa} com sucesso!\n")


def devolver_livro(livros):
    codigo = ler_inteiro("Digite o código do livro que deseja devolver: ")
    livro = buscar_livro(livros, codigo)

    if livro is None:
        print("Livro não encontrado.\n")
    elif livro["disponivel"]:
        print("Este livro já está na estante (não consta como emprestado).\n")
    else:
        livro["disponivel"] = True
        livro["emprestado_para"] = None
        print(f"O livro '{livro['titulo']}' foi devolvido com sucesso!\n")


def main():
    livros = carregar_livros()

    while True:
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            cadastrar_livro(livros)
            salvar_livros(livros)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            emprestar_livro(livros)
            salvar_livros(livros)
        elif opcao == "4":
            devolver_livro(livros)
            salvar_livros(livros)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")


main()
