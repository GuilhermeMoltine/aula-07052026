import sqlite3

class FilmeRepository:

    def salvar(self, filme):
        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        cursor.execute("""
        INSERT INTO filmes (titulo, duracao, genero)
        VALUES (?, ?, ?)
        """, (filme.titulo, filme.duracao, filme.genero))

        conexao.commit()
        conexao.close()