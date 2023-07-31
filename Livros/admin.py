from django.contrib import admin
from .models import Livros, Cadastro, Filmes

@admin.register(Livros)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao','autor','ano_lancamento', 'imagem',)
    
@admin.register(Cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email','senha',)

@admin.register(Filmes)
class FilmesAdmin(admin.ModelAdmin):
    list_display = ('titulo','ano_lancamento','resumo','imagem', 'assistir',)