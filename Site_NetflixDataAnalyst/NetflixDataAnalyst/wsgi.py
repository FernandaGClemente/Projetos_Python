"""
WSGI config for NetflixDataAnalyst project.
Configuração WSGI para o projeto NetflixDataAnalyst.
It exposes the WSGI callable as a module-level variable named ``application``.
Ele expõe o callable WSGI como uma variável de nível de módulo chamada ``application``.
For more information on this file, see
Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NetflixDataAnalyst.settings')

application = get_wsgi_application()
