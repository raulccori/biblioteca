import sqlite3

def criar_tabela():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano INTEGER,
            disponivel TEXT
            )
        """)
        conexao.commit()
    except Exception as erro:
        #Caso ocorra algum erro no banco
        print(f"erro ao tentar criar a tabela {erro}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()
criar_tabela()

def cadastrar_livro(titulo, autor, ano):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO livros(titulo, autor, ano, disponivel)
            VALUES (?, ?, ?, ?)
            """, (titulo, autor, ano, "sim")
            )
        conexao.commit()
    except Exception as erro:
        print(f"erro ao tentar cadastrar livro {erro}")
    finally:
        if conexao:
            conexao.close()

cadastrar_livro("hora do espanto", "raul", 2015)


def lista_livros():
    try:
        conexao = sqlite3.connect('biblioteca.db')
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros")
        for livro in cursor.fetchall():
            print(f"ID: {livro[0]}, Título: {livro[1]}, Autor: {livro[2]}, Ano: {livro[3]}, Disponível: {livro[4]}")
    except sqlite3.Error as error:
        print("Erro ao listar livros:", error)
    finally:
        if conexao:
            conexao.close()

lista_livros()

