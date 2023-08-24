from django.db import models

class Filme(models.Model):
    id_filme = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=50)
    descrição = models.TextField(max_length=255)
    duração = models.FloatField()