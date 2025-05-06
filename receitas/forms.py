from django import forms
from .models import Receita, Categoria

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['titulo', 'ingredientes', 'modo_preparo', 'tempo_preparo', 
                 'rendimento', 'dificuldade', 'categoria', 'imagem']
        widgets = {
            'ingredientes': forms.Textarea(attrs={'rows': 4}),
            'modo_preparo': forms.Textarea(attrs={'rows': 6}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']