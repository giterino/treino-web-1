from django.db import models

# Create your models here.

class Docente(models.Model):
    nome = models.CharField(max_length=64)
    nusp = models.IntegerField()

    def __str__(self):
        return f"Docente {self.id}: {self.nusp}, {self.nome}"

class Aluno(models.Model):
    nome = models.CharField(max_length=64)
    nusp = models.IntegerField()
    orientador = models.ForeignKey(
        Docente,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name="orientandos",
    )

    def __str__(self):
        return f"Aluno {self.id}: {self.nusp}, {self.nome}"
