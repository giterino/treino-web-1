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

class Relatorio(models.Model):
    periodo = models.IntegerField()
    nro_tentativa = models.IntegerField()
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name="relatorios",
    )
    docente_responsavel = models.ForeignKey(
        Docente,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name="relatorios",
    )
    class Status(models.IntegerChoices):
        VAZIO = 0
        PREENCHIDO = 1
        AVALIADO_POR_DOCENTE = 2
        AVALIADO_POR_CCP = 3
    status = models.IntegerField(choices=Status.choices)
    # TODO: adicionar campos preenchidos por aluno
    nro_artigos_aceitos = models.IntegerField(null=True, blank=True)
    atividades_academicas = models.TextField(null=True, blank=True)
    atividades_pesquisa = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"periodo={self.periodo}, aluno={self.aluno.nome}, {self.status}"

    def rotulo_status(self):
        return self.Status(self.status).label

class Avaliacao(models.Model):
    relatorio = models.ForeignKey(
        Relatorio,
        on_delete=models.CASCADE,
        related_name="avaliacoes",
    )
    avaliador = models.ForeignKey(
        Docente,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name="avaliacoes",
    )
    parecer = models.CharField(max_length=255)
    class Conceito(models.IntegerChoices):
        ADEQUADO = 0
        ADEQUADO_COM_RESSALVAS = 1
        INSATISFATORIO = 2
    conceito = models.IntegerField(choices=Conceito.choices)

    def __str__(self):
        return f"relatorio_id={self.relatorio.id} avaliador={self.avaliador.nome} conceito={self.conceito}"

    def rotulo_conceito(self):
        return self.Conceito(self.conceito).label
