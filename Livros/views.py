from django.shortcuts import render, get_object_or_404,redirect
from .models import Livros, Cadastro, Filmes
from .forms import LivrosForm, CadastroForm, FilmesForm
# from  django.contrib.auth import authenticate
# from  django.contrib.auth import login as loginho
# from django.contrib.auth.models import User
# from django.contrib import messages


def index(request):
   
    return render(request,"Livros/index.html")

def cadastrar_livros(request):
    if request.method == 'POST':
        form = LivrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = LivrosForm()
            
    else:
        form = LivrosForm()
    
    return render(request, "Livros/form.html", {'form':form})

def listar_livros(request):
    livros = Livros.objects.all()
    context = {
        'livros':livros
    }
    return render (request, 'Livros/listar.html', context)

def detalhar_livros(request,id):
    livros = get_object_or_404(Livros, id=id)
    context={'livros':livros}
    return render (request, 'Livros/detalhar.html', context)



def remover_livro(request, id):
    livro = get_object_or_404(Livros, id=id)
    livro.delete()
    return redirect('listar_livros')



def editar_livro(request,id):
    livro = get_object_or_404(Livros,id=id)
   
    if request.method == 'POST':
        form = LivrosForm(request.POST,request.FILES,instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivrosForm(instance=livro)

    return render(request,'Livros/form.html',{'form':form})



#FILMES

def editar_filme(request, id):
    filme = get_object_or_404(Filmes, id=id)
    
    if request.method == 'POST':
        form =FilmesForm(request.POST, request.FILES, instance=filme)
        
        if form.is_valid():
            form.save()
            return redirect ('listar_filmes')            
    else:   
        form =FilmesForm(instance=filme)
        
    return render (request, 'filmes/form.html',{'form':form})

def listar_filmes(request):
    filmes = Filmes.objects.all()
    context={
        'filmes':filmes
    }
    return render (request, 'filmes/listar.html', context)

def cadastrar_filmes(request):
    if request.method == 'POST':
        form = FilmesForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            form = FilmesForm()
    else:
        form =FilmesForm()
        
    return render(request, 'filmes/form.html', {'form':form})


def apagar_filmes(request, id):
    filme = get_object_or_404(Filmes, id=id)
    filme.delete()
    return redirect('listar_filmes')   


def detalhar_filmes(request, id):
    filme = get_object_or_404(Filmes, id=id)
    context={'filme':filme}
    return render (request, 'filmes/detalhar.html', context)