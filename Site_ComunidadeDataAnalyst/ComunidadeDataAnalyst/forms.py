from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from ComunidadeDataAnalyst.models import Usuario
from flask_login import current_user


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_enviar_login = SubmitField('Fazer login')


class FormCadastroConta(FlaskForm):
    username = StringField('Nome do Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de senha', validators=[DataRequired(), EqualTo('senha')])
    botao_enviar_cadastro_conta = SubmitField('Cadastrar conta')

    # noinspection PyMethodMayBeStatic
    def validate_email(self, email):
        # Verifica se o email que esta sendo cadastrado já existe no banco de dados
        # Faça uma consulta nos cadastros dos usuários filtrando pelo email no banco de bados
        # e atribua o resultado na variavel usuario
        usuario = Usuario.query.filter_by(email=email.data).first()
        # Se a resposta for True, ou seja, o email já está cadastrado no banco de dados:
        if usuario:
            # Informe o erro
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome do Usuário:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil:', validators=[FileAllowed(['jpg', 'png'])])
    curso_excel = BooleanField('Microsoft Excel')
    curso_python = BooleanField('Linguagem Python')
    curso_powerbi = BooleanField('Microsoft Power BI')
    curso_sql = BooleanField('Linguagem SQL')
    curso_estatistica = BooleanField('Estatística')
    curso_outros = BooleanField('Outros cursos')
    botao_enviar_editar_perfil = SubmitField('Confirmar edição')

    # noinspection PyMethodMayBeStatic
    def validate_email(self, email):
        # Verficar se o email que está sendo alterado na edição do perfil existe no banco de dados
        # Se o email do usuario atual for diferente do email do banco de dados
        if current_user.email != email.data:
            # Faça uma consulta nos cadastros dos usuários filtrando pelo email no banco de bados
            # e atribua o resultado na variavel usuario
            usuario = Usuario.query.filter_by(email=email.data).first()
            # Se a resposta for True, ou seja, o email já está cadastrado no banco de dados:
            if usuario:
                # Informe o erro
                raise ValidationError('Já existe um usuario com esse e-mail. Cadastre outro e-mail')


class FormCriarPost(FlaskForm):
    titulo = StringField('Titulo do Post', validators=[DataRequired(), Length(6, 140)])
    corpo = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    botao_enviar_post = SubmitField('Criar post')
