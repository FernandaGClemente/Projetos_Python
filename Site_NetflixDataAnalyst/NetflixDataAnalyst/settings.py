"""
Django settings for NetflixDataAnalyst project.
Configurações do Django para o projeto NetflixDataAnalyst.
Generated by 'django-admin startproject' using Django 4.1.7.
Gerado por 'django-admin startproject' usando Django 4.1.7.

For more information on this file, see
Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
Para obter a lista completa de configurações e seus valores, consulte
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Variável constante (Que não muda de valor) do diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings — unsuitable for production
# Configurações de desenvolvimento de início rápido — inadequadas para produção
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# AVISO DE SEGURANÇA: mantenha a chave secreta usada na produção em segredo!
SECRET_KEY = 'django-insecure-n@odx2=8c@5f*q@&_yztt(^z7w@so@#kfv=ht0wyl8j_wy%h3-'

# SECURITY WARNING: don't run with debug turned on in production!
# AVISO DE SEGURANÇA: não execute com o debug ativado na produção!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition (Definição de aplicativo)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'filme',
    'crispy_forms',
    'crispy_bootstrap5'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
# variável que gerencia as URLS (links)
ROOT_URLCONF = 'NetflixDataAnalyst.urls'

# modelos das páginas html
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'filme.novos_context.lista_filmes_novos',
                'filme.novos_context.lista_filmes_populares'
            ],
        },
    },
]
# variável que gerencia o servidor
WSGI_APPLICATION = 'NetflixDataAnalyst.wsgi.application'


# Database (Banco de Dados)
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation (Validação de senha)
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_USER_MODEL = "filme.Usuario"
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization (Internacionalização)
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) — Pasta onde ficará os arquivos estáticos
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / "media"

# Default primary key field type (Campo Chave Primária Padrão)
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuração dos bloqueios das páginas sem login
# URL da página que o usuario será direcionado quando realizar o login
LOGIN_REDIRECT_URL = 'filme:homefilmes'
# URL da página para o usuario realizar o login
LOGIN_URL = 'filme:login'

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'