
from django.contrib import admin
from django.urls import path
from Livros.views import index, cadastrar_livros,listar_livros,detalhar_livros,remover_livro,editar_livro, listar_filmes, cadastrar_filmes, apagar_filmes, editar_filme, detalhar_filmes
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('form/',cadastrar_livros, name="cadastro_livros" ),
    path('livros/', listar_livros, name='listar_livros'),
    path('detalhar/<int:id>/',detalhar_livros, name='detalhar_livros' ),
    path('apagar/<int:id>/', remover_livro, name='remover_livro'),
    path('editar/<int:id>/', editar_livro, name='editar_livro'),
    
    #filmes

    path('form/filme', cadastrar_filmes, name='cadastrar_filmes'),
    path('listar_filmes/', listar_filmes, name='listar_filmes'),
    path('apagar/filme/<int:id>/', apagar_filmes, name='apagar_filmes'),
    path('editar/filme/<int:id>/', editar_filme, name='editar_filme'),
    path('detalhar/filme/<int:id>/', detalhar_filmes, name='detalhar_filmes')
    
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




