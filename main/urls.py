
from django.contrib import admin
from django.urls import path
from Livros.views import index, cadastrar_livros,listar_livros,detalhar_livros,remover_livro,editar_livro
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('form/',cadastrar_livros, name="cadastro_livros" ),
    path('livros/', listar_livros, name='listar_livros'),
    path('detalhar/<int:id>/',detalhar_livros, name='detalhar_livros' ),
    path('apagar/<int:id>/', remover_livro, name='remover_livro'),
    path('editar/<int:id>/', editar_livro, name='editar_livro')
    
    
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)




