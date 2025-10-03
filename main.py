import sqlite3

def criar_tabela():
    try:
        conexao = sqlite3.connet("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos(
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
        print(f"erro ao tentar excluir aluno {erro}")
    finally:
        #Sempre fechar a conexão
        if conexao:
            conexao.close()
criar_tabela()