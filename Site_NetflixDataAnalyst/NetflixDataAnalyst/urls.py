"""NetflixDataAnalyst URL Configuration
Configuração de URL do NetflixDataAnalyst
The `urlpatterns` list routes URLs to views. For more information please see:
A lista `urlpatterns` roteia URLs para visualizações. Para mais informações consulte:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Exemplos:
Function views
Visualizações de funções
    1. Add an import:  from my_app import views
    1. Adicione uma importação: das exibições de importação my_app
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
    2. Adicione um URL a urlpatterns: path('', views.home, name='home')
Class-based views
Visualizações baseadas em classe
    1. Add an import:  from other_app.views import Home
    1. Adicione uma importação: from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    2. Adicione um URL a urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
Incluindo outro URLconf
    1. Import the include() function: from django.urls import include, path
    1. Importe a função include(): from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    2. Adicione um URL a urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Configuração das URLS (urlpatterns = padrões de url)
urlpatterns = [
    # Caminho da URLs do site de administração será admin/
    path('admin/', admin.site.urls),
    # Caminho da URLs das páginas dos "filmes" (Estarão config na urls.py da app Filme) será vazia ('')
    # Partindo do presuposto que o nome da app é "filme"
    path('', include('filme.urls', namespace='filme'))
]

# A imagem do site pode ser aberta numa nova guia: "Abrir imagem numa nova guia" > A imagem é armazenada num link.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
