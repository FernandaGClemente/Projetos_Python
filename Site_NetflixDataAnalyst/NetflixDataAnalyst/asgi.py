"""
ASGI config for NetflixDataAnalyst project.
Configuração ASGI para o projeto NetflixDataAnalyst.
It exposes the ASGI callable as a module-level variable named ``application``.
Ele expõe o ASGI chamável como uma variável de nível de módulo chamada ``application``.
For more information on this file, see
Para obter mais informações sobre este arquivo, consulte
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NetflixDataAnalyst.settings')

application = get_asgi_application()
