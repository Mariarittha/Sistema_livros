from django.db import models

# Create your models here.
class Cadastro (models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    senha = models.IntegerField()
    
    
class Livros (models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField
    autor = models.CharField(max_length=120)
    ano_lancamento = models.IntegerField(null='')
    imagem = models.ImageField(upload_to='img')
    
