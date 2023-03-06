from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '651bb75489ae2cc3cbc5668710646384'

if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ComunidadeDataAnalyst.db'

database = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from ComunidadeDataAnalyst import models  # noqa: E402

engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
insp = sqlalchemy.inspect(engine)
if not insp.has_table("usuario"):
    with app.app_context():
        database.drop_all()
        database.create_all()
    print('Banco de Dados criado')
else:
    print('Base de Dados já existe')


from ComunidadeDataAnalyst import routes  # noqa: E402
