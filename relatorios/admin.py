from django.contrib import admin

from .models import Docente, Aluno, Relatorio, Avaliacao

# Register your models here.
admin.site.register(Docente)
admin.site.register(Aluno)
admin.site.register(Relatorio)
admin.site.register(Avaliacao)
