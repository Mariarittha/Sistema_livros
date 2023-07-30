from django.contrib import admin
from .models import Livros, Cadastro

@admin.register(Livros)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao','autor','ano_lancamento', 'imagem',)
    
@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email','senha',)

