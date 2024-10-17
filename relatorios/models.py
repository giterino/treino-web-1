from django.db import models

# Create your models here.

class Docente(models.Model):
    nome = models.CharField(max_length=64)
    nusp = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.nusp}, {self.nome}"
