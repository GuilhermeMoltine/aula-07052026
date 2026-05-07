from model.filme import Filme

class FilmeView:

    def cadastrar_filme(self):
        titulo = input("Título: ")
        duracao = input("Duração: ")
        genero = input("Gênero: ")

        return Filme(titulo, duracao, genero)