from models.usuario_models import Usuario
from repositories.usuario_repositories import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastro = self.repository.pesquisar_usuario_por_email(email=usuario.email)

            if cadastro:
                print("Usuário já foi cadastrado")
                return
            
            self.repository.salvar_usuario(usuario=usuario)
            print("Usuário cadastrado com sucesso1")
        except TypeError as erro:
            print("Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print("Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()