from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin


# Como foi adicionado a coluna filmes_vistos na classe Usuario
# (No modelo de usuario configurado do Django não tem esta coluna)
# é necessário adicionar esse campo dentro do gerenciador do admin
campos = list(UserAdmin.fieldsets)
campos.append(('Histórico', {'fields': ('filmes_vistos',)}))
UserAdmin.fieldsets = tuple(campos)

# Registre no site na conta do administrador no aplicativo de Filme a tabela Filme
admin.site.register(Filme)
# Registre no site na conta do administrador no aplicativo de Filme a tabela Episodio
admin.site.register(Episodio)
# Registre no site na conta do administrador no aplicativo de Filme a tabela Usuario
admin.site.register(Usuario, UserAdmin)
