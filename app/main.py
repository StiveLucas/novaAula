from services.usuario_service import UsuarioService
from repositories.usuario_repositories import UsuarioRepository
from config.database import session
import os

def main():
    Session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    #Solicitando dados do usuario.
    print("\nAdcionando usuário: ")
    nome = input("Digite o nome do usuário: ")
    email = input("Digite o email do usuário: ")
    senha = input("Digite a senha do usuário: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    #Exibindo todos os usuário na tabela do banco de dados.
    print("\nListando usuário cadastrados: ")
    lista_usuario = service.listar_todos_usuarios()
    for usuario in lista_usuario:
        print(f"Nome: {usuario.nome} \nE-mail: {usuario.email} \nSenha: {usuario.senha} \n\n")

if __name__ == "__main__":
    os.system("cls || clear")
    main()