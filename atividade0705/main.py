from view.filme_view import FilmeView
from repository.filme_repository import FilmeRepository
from service.filme_service import FilmeService
from controller.filme_controller import FilmeController


view = FilmeView()

repository = FilmeRepository()

service = FilmeService(repository)

controller = FilmeController(service)


filme = view.cadastrar_filme()

controller.cadastrar(filme)

print("Filme cadastrado com sucesso!")