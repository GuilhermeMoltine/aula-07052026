class FilmeService:

    def __init__(self, repository):
        self.repository = repository

    def cadastrar_filme(self, filme):
        self.repository.salvar(filme)