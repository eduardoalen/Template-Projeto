from django.contrib import admin
from .models import Receita, Categoria

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'dificuldade_display', 'tempo_preparo', 'data_criacao')
    list_filter = ('categoria', 'dificuldade', 'data_criacao')
    search_fields = ('titulo', 'ingredientes', 'modo_preparo')
    
    def dificuldade_display(self, obj):
        return obj.get_dificuldade_display()
    dificuldade_display.short_description = 'Dificuldade'

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)