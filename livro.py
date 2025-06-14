# livro.py
import sqlite3
from datetime import datetime

class Livro:
    def __init__(self, titulo, autor, editora, paginas, descricao, data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
        self.descricao = descricao
        self.data_publicacao = data_publicacao

class Livraria:
    def __init__(self, nome_banco="livros.db"):
        self.conn = sqlite3.connect(nome_banco)
        self.cursor = self.conn.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS livro (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            editora TEXT,
            paginas INTEGER NOT NULL,
            descricao TEXT,
            dataPublicacao DATE NOT NULL
        )
        ''')
        self.conn.commit()

    def adicionar(self, livro: Livro):
        try:
            if not isinstance(livro.paginas, int):
                raise ValueError("Número de páginas deve ser inteiro.")
            datetime.strptime(livro.data_publicacao, "%Y-%m-%d")
            self.cursor.execute('''
                INSERT INTO livro (titulo, autor, editora, paginas, descricao, dataPublicacao)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (livro.titulo, livro.autor, livro.editora, livro.paginas, livro.descricao, livro.data_publicacao))
            self.conn.commit()
            print("✅ Livro adicionado com sucesso!\n")
        except ValueError as e:
            print(f"❌ Erro ao adicionar livro: {e}\n")
            raise

    def listar(self):
        self.cursor.execute("SELECT * FROM livro")
        return self.cursor.fetchall()

    def buscar_por_id(self, id):
        self.cursor.execute("SELECT * FROM livro WHERE id=?", (id,))
        return self.cursor.fetchone()

    def atualizar(self, id, livro: Livro):
        try:
            datetime.strptime(livro.data_publicacao, "%Y-%m-%d")
            self.cursor.execute('''
                UPDATE livro
                SET titulo=?, autor=?, editora=?, paginas=?, descricao=?, dataPublicacao=?
                WHERE id=?
            ''', (livro.titulo, livro.autor, livro.editora, livro.paginas, livro.descricao, livro.data_publicacao, id))
            self.conn.commit()
            print("✅ Livro atualizado com sucesso!\n")
        except ValueError:
            print("❌ Data inválida! Use o formato YYYY-MM-DD.\n")

    def deletar(self, id):
        try:
            if not isinstance(id, int) or id <= 0:
                  raise ValueError("ID inválido. O ID deve ser um número inteiro positivo.")
             
            self.cursor.execute("SELECT * FROM livro WHERE id=?", (id,))
            if self.cursor.fetchone() is None:     
                print(f"❌ Nenhum livro encontrado com o ID {id}.\n")
                return
            self.cursor.execute("DELETE FROM livro WHERE id=?", (id,))
            self.conn.commit()
        except ValueError as e:
            print(f"❌ Erro ao deletar livro: {e}\n")

    def fechar(self):
        self.conn.close()