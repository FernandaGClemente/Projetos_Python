from flask import render_template, redirect, url_for, flash, request, abort
from ComunidadeDataAnalyst import app, database, bcrypt
from ComunidadeDataAnalyst.forms import FormLogin, FormCadastroConta, FormEditarPerfil, FormCriarPost
from ComunidadeDataAnalyst.models import Usuario, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image


@app.route('/')
@app.route('/home')
def home():
    posts = Post.query.order_by(Post.id.desc())
    #  para utilizar a variável criada no html temos que incluí-la no render_template
    return render_template('home.html', posts=posts)


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
    lista_usuarios = Usuario.query.all()
    #  para utilizar a lista de usuários criada no html temos que incluí-la no render_template
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_cadastroconta = FormCadastroConta()

    if form_login.validate_on_submit() and 'botao_enviar_login' in request.form:
        # Verificar se o usuário existe e se a senha digitada é igual a que foi inserida no banco de dados
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            # Realizará o login do usuário e
            # verificará se está acionado ou não o campo "Lembrar dados" para manter os dados preenchidos
            login_user(usuario, remember=form_login.lembrar_dados.data)
            # Exibir mensagem de sucesso
            flash(f'Login feito com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            # Redirecionar para a homepage ou para a página que o user estava tentando acessar antes de estar logado
            # Realizando uma requisição dos argumentos do parâmetro Next,
            # pegando-os e armazendo na variável parametro_next
            parametro_next = request.args.get('next')
            # Se o parametro next existir (parametro_next = True),
            # redirecione para a página que estava sendo acessada
            if parametro_next:
                return redirect(parametro_next)
            # Caso contrario, redirecione para a homepage
            else:
                # Redirecionar para a homepage
                return redirect(url_for('home'))
        else:
            # Exibir mensagem de erro
            flash(f'Falha no login. E-mail ou senha incorretos', 'alert-danger')

    if form_cadastroconta.validate_on_submit() and 'botao_enviar_cadastro_conta' in request.form:
        # Criptografia da senha
        senha_cript = bcrypt.generate_password_hash(form_cadastroconta.senha.data).decode("utf-8")
        # Criar a conta do usuário
        usuario = Usuario(username=form_cadastroconta.username.data,
                          email=form_cadastroconta.email.data,
                          senha=senha_cript)
        # Adicionar no banco de dados o usuário
        database.session.add(usuario)
        # Salvar as informações do usuário
        database.session.commit()
        # Exibir mensagem de sucesso
        flash(f'Conta criada para o e-mail: {form_cadastroconta.email.data}', 'alert-success')
        # Redirecionar para a homepage
        return redirect(url_for('home'))
    #  para utilizar os formulários criados no html temos que incluí-los no render_template
    return render_template('login.html', form_login=form_login, form_cadastroconta=form_cadastroconta)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    # Exibir mensagem de sucesso
    flash(f'logout feito com sucesso', 'alert-success')
    # Redirecionar para a homepage
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def perfil():
    #  variavel = url_for("Pasta", filename = "subpasta/arquivo.png")
    #  arquivo.png = Acessará na coluna foto_perfil da tabela Usuarios a foto do usuário atual
    foto_perfil = url_for('static', filename = 'fotos_perfil/{}'.format(current_user.foto_perfil))
    #  para utilizar a variável criada no html temos que incluí-la no render_template
    return render_template('perfil.html', foto_perfil=foto_perfil)


@app.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def exibir_post(post_id):
    post = Post.query.get(post_id)
    # Se o usuário atual é igual ao autor do post
    if current_user == post.autor:
        # Exibirá o formulário de criar post para alterar as informações
        form_criarpost = FormCriarPost()
        # Quando quiser que o titulo e o corpo do post já apareçam preenchido ao acessar o formulário de criação de post
        if request.method == 'GET':
            form_criarpost.titulo.data = post.titulo
            form_criarpost.corpo.data = post.corpo
        # Se a validação de email criada no forms.py for validada:
        elif form_criarpost.validate_on_submit():
            post.titulo = form_criarpost.titulo.data
            post.corpo = form_criarpost.corpo.data
            # Salvar as informações da publicação
            database.session.commit()
            # Exibir mensagem de sucesso
            flash('Post atualizado com sucesso!', 'alert-success')
            # Redirecionar para a homepage
            return redirect(url_for('home'))
    else:
        # Caso não seja, não aparecerá o formulário
        form_criarpost = None
    #  para utilizar o formulário criado no html temos que incluí-lo no render_template
    return render_template('post.html', post=post, form_criarpost=form_criarpost)


@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def criar_post():
    form_criarpost = FormCriarPost()
    # Se a validação de email criada no forms.py for validada:
    if form_criarpost.validate_on_submit():
        post = Post(titulo=form_criarpost.titulo.data, corpo=form_criarpost.corpo.data, autor=current_user)
        # Adicionar no banco de dados a publicação
        database.session.add(post)
        # Salvar as informações da publicação
        database.session.commit()
        # Exibir mensagem de sucesso
        flash('Post criado com sucesso', 'alert-success')
        # Redirecionar para a homepage
        return redirect(url_for('home'))
    #  para utilizar o formulário criado no html temos que incluí-lo no render_template
    return render_template('criarpost.html', form_criarpost=form_criarpost)


@app.route('/post/<post_id>/excluir', methods=['GET', 'POST'])
@login_required
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash('Post excluido com sucesso', 'alert-success')
        return redirect(url_for('home'))
    else:
        abort(403)


def salvar_imagem(imagem):
    # Adicionar um código aleatório no nome da imagem para torna-la única (Ex: NomeDaImagem8n°aleatórios.extensão)
    codigo = secrets.token_hex(8)  # Criação do código aleátio de 8 números
    nome, extensao = os.path.splitext(imagem.filename)  # Armazenando o nome e a extensão da imagem nas variáveis
    nome_arquivo = nome + codigo + extensao  # Armazendo na variável o nome, o código e a extensão
    # app.root_path é o caminho da pasta ComunidadeDataAnalyst
    # Armazendo na variável o caminho "app.root_path" + o caminho 'static/fotos_perfil' + nome dos arquivos
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', nome_arquivo)
    # Reduzir o tamanho da imagem
    tamanho = (200, 200)  # Definindo que o tamanho será de 200 (altura, largura)
    imagem_reduzida = Image.open(imagem)  # Abrindo a imagem e armazendo na variavel imagem_reduzida
    imagem_reduzida.thumbnail(tamanho)  # Reduzindo a imagem para o tamanho defindo (miniatura)
    # Salvar a imagem inserida na pasta fotos_perfil
    imagem_reduzida.save(caminho_completo)  # Salvando a imagem reduzida no caminho definido
    return nome_arquivo


def atualizar_cursos(form_editarperfil):
    lista_cursos = []
    for campo in form_editarperfil:  # Para cada campo no formulário
        if 'curso_' in campo.name:  # Se o nome do campo for "curso_":
            if campo.data:  # Se o curso estiver selecionado (caixa de seleção esteja marcado) faça:
                # Adicionar o texto do campo.label (rótulo) na lista de cursos
                lista_cursos.append(campo.label.text)
    return ';'.join(lista_cursos)  # Junte cada texto com um ;


@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form_editarperfil = FormEditarPerfil()
    # Se a validação de email criada no forms.py for validada:
    if form_editarperfil.validate_on_submit():
        # O username inserido pelo usuario atual no formulario será o novo username do banco de dados
        current_user.username = form_editarperfil.username.data
        # O email inserido pelo usuario atual no formulario será o novo email do banco de dados
        current_user.email = form_editarperfil.email.data
        # Se foto_perfil inserido pelo usuario atual for alterado no formulário
        if form_editarperfil.foto_perfil.data:
            # Armazena na variável o nome do arquivo da imagem inserida pelo usuario atual
            # na coluna foto_perfil do banco de dados já reduzida e codificada
            nome_imagem = salvar_imagem(form_editarperfil.foto_perfil.data)
            # Mudar o campo foto_perfil do usuário para o novo nome da imagem
            current_user.foto_perfil = nome_imagem
        # As seleções dos cursos pelo usuário atual for alterado no formulário
        current_user.cursos = atualizar_cursos(form_editarperfil)
        # Salvar as informações no usuário
        database.session.commit()
        # Exibir mensagem de sucesso
        flash(f'Perfil atualizado com sucesso', 'alert-success')
        # Redirecionar para a página de perfil
        return redirect(url_for('perfil'))
    # Quando quiser que o nome e o email do usuário já apareçam preenchido ao acessar o formulário de edição do perfil
    elif request.method == 'GET':
        form_editarperfil.email.data = current_user.email
        form_editarperfil.username.data = current_user.username

    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    #  para utilizar a variável criada e o formulário criado no html temos que incluí-los no render_template
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form_editarperfil=form_editarperfil)
