from django.db import models
from django.contrib import admin
# Create your models here.

class Formulario(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    data_criacao = models.DateField("data_criacao")
    ativo = models.BooleanField(default=True)
    
    @admin.display(
        boolean=False,
        ordering="data_criacao",
        description="Published recently?",
    )
    
    def __str__(self):
        return self.nome