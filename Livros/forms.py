from django.forms import ModelForm
from django import forms
from .models import Livros, Cadastro

class LivrosForm(ModelForm):
    class Meta:
        model = Livros
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control' }),
            'ano_lancamento': forms.TextInput(attrs={'class': 'form-control'}),
            'imagem ': forms.FileInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control'}),
            'descricao': forms.Textarea(attrs={'class':'form-control'}) 
        }
class CadastroForm (ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'
        widgets ={
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'senha': forms.PasswordInput(attrs={'class':'form-control'})
    }
        
    