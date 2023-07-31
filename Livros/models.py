from django.db import models

# Create your models here.
class Cadastro (models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    senha = models.IntegerField()
    
    
class Livros (models.Model):
    nome = models.CharField(max_length=120)
    autor = models.CharField(max_length=120)
    descricao = models.CharField(max_length=500)

    ano_lancamento = models.IntegerField(null='')
    imagem = models.ImageField(upload_to='img')
    

class Filmes(models.Model):
    titulo = models.CharField(max_length=120)
    ano_lancamento = models.IntegerField()
    resumo = models.CharField(max_length=600)
    assistir = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='images')