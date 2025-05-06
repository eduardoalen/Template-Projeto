from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome

class Receita(models.Model):
    DIFICULDADE_CHOICES = [
        ('F', 'Fácil'),
        ('M', 'Médio'),
        ('D', 'Difícil'),
    ]
    
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.PositiveIntegerField(help_text="Tempo em minutos")
    rendimento = models.CharField(max_length=100)
    dificuldade = models.CharField(max_length=1, choices=DIFICULDADE_CHOICES)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='receitas/', blank=True, null=True)
    
    def __str__(self):
        return self.titulo
    
    @property
    def dificuldade_display(self):
        return dict(self.DIFICULDADE_CHOICES).get(self.dificuldade, '')
    
    class Meta:
        ordering = ['-data_criacao']