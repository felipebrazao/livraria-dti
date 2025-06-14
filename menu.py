from livro import Livro, Livraria

def input_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Este campo é obrigatório. Tente novamente.")

def input_inteiro(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor.isdigit() and int(valor) > 0:
            return int(valor)
        print("Insira um número inteiro positivo.")

def input_data(mensagem):
    while True:
        valor = input(mensagem).strip()
        try:
            datetime.strptime(valor, "%Y-%m-%d")
            return valor
        except ValueError:
            print("Data inválida! Use o formato YYYY-MM-DD.")

def obter_livro_input(padrao=None):
    if padrao:
        titulo = input_obrigatorio(f"Título [{padrao[1]}]: ") or padrao[1]
        autor = input_obrigatorio(f"Autor [{padrao[2]}]: ") or padrao[2]
        editora = input(f"Editora [{padrao[3]}] (opcional): ") or padrao[3]
        paginas = input_inteiro(f"Páginas [{padrao[4]}]: ") or padrao[4]
        descricao = input(f"Descrição [{padrao[5]}] (opcional): ") or padrao[5]
        data_publicacao = input_data(f"Data de Publicação [{padrao[6]}] (YYYY-MM-DD): ") or padrao[6]
    else:
        titulo = input_obrigatorio("Título: ")
        autor = input_obrigatorio("Autor: ")
        editora = input("Editora (opcional): ")
        paginas = input_inteiro("Número de páginas: ")
        descricao = input("Descrição (opcional): ")
        data_publicacao = input_data("Data de publicação (YYYY-MM-DD): ")

    return Livro(titulo, autor, editora, paginas, descricao, data_publicacao)

def mostrar_menu():
    print("\nMENU LIVRARIA")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar por ID")
    print("4. Atualizar livro")
    print("5. Deletar livro")
    print("6. Sair")

def main():
    sistema = Livraria()

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            livro = obter_livro_input()
            sistema.adicionar(livro)

        elif escolha == '2':
            livros = sistema.listar()
            if livros:
                for l in livros:
                    print(f"\nID: {l[0]}")
                    print(f"Título: {l[1]}")
                    print(f"Autor: {l[2]}")
                    print(f"Editora: {l[3] or 'Não informado'}")
                    print(f"Páginas: {l[4]}")
                    print(f"Descrição: {l[5] or 'Não informado'}")
                    print(f"Publicado em: {l[6]}")
            else:
                print("Nenhum livro cadastrado.\n")

        elif escolha == '3':
            id = input("Digite o ID do livro: ")
            if id.isdigit():
                livro = sistema.buscar_por_id(id)
                if livro:
                    print(f"\nTítulo: {livro[1]}")
                    print(f"Autor: {livro[2]}")
                    print(f"Editora: {livro[3] or 'Não informado'}")
                    print(f"Páginas: {livro[4]}")
                    print(f"Descrição: {livro[5] or 'Não informado'}")
                    print(f"Publicado em: {livro[6]}")
                else:
                    print("Livro não encontrado.\n")
            else:
                print("ID inválido.\n")

        elif escolha == '4':
            id = input("Digite o ID do livro a atualizar: ")
            if id.isdigit():
                id_int = int(id)
                atual = sistema.buscar_por_id(id)
                if atual:
                    livro = obter_livro_input(atual)
                    sistema.atualizar(id, livro)
                else:
                    print("Livro não encontrado.\n")
            else:
                print("ID inválido.\n")

        elif escolha == '5':
            id = input("Digite o ID do livro a deletar: ")
            if id.isdigit():
                id_int = int(id)
                if sistema.buscar_por_id(id_int):
                     sistema.deletar(id_int)
                     print("Livro deletado com sucesso!\n")
                else:
                    print("Livro não encontrado.\n")  
            else:
                print("ID inválido.\n")       
        elif escolha == '6':
            print("Saindo do sistema...")
            sistema.fechar()
            break
        else:
            print("Opção inválida. Escolha de 1 a 6.\n")

if __name__ == "__main__":
    from datetime import datetime
    main()