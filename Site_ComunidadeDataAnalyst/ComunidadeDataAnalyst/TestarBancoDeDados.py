from ComunidadeDataAnalyst.models import Usuario, Post
from ComunidadeDataAnalyst import app


# Criação e ativação do Banco de Dados "ComunidadeDataAnalyst.db"
# with app.app_context():
#    database.create_all()


# Criação de um usuário administrador
# with app.app_context():
# Inserindo as informações do usuario
#    var_usuario_adm = Usuario(username='Usuario Teste', email='usuarioteste@hotmail.com', senha='123456')
# Adicionar no Banco de Dados
#    database.session.add(var_usuario_adm)
# Gravar no Banco de Dados
#    database.session.commit()

# Consultando as informações do primeiro usuario cadastrado
with app.app_context():
    lista_usuarios_cadastrados = Usuario.query.all()
    print(lista_usuarios_cadastrados)

    primeiro_usuario = Usuario.query.first()
    print(primeiro_usuario.id)
    print(primeiro_usuario.username)
    print(primeiro_usuario.email)
    print(primeiro_usuario.senha)
    print(primeiro_usuario.foto_perfil)
    print(primeiro_usuario.cursos)

# Consultando as informações do usuario com o email = usuarioteste@hotmail.com
# with app.app_context():
#    lista_usuarios_cadastrados = Usuario.query.all()
#    usuario_teste = Usuario.query.filter_by(email='usuarioteste@hotmail.com').first()
#    print(usuario_teste)
#    print(usuario_teste.id)
#    print(usuario_teste.username)
#    print(usuario_teste.senha)

# with app.app_context():
#     database.drop_all()
#     database.create_all()

# Consultando as informações do primeiro post cadastrado
with app.app_context():
    lista_post_cadastrados = Post.query.all()
    print(lista_post_cadastrados)

    primeiro_post = Post.query.first()
    print(primeiro_post.titulo)
    print(primeiro_post.corpo)

# Este é o primeiro post da comunidade
# Este é um projeto com objetivo de mostrar as habilidades em Python
# utilizando as bibliotecas de Desenvolvimento WEB
# na criação de uma comunidade fictícia de analistas de dados.
