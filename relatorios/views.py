from django.shortcuts import render
from .models import Docente, Aluno, Relatorio

# Create your views here.

def lista_docente(request):
    return render(request, "relatorios/lista_docente.html", {
        "docentes": Docente.objects.all()
    })

def docente(request, docente_id):
    docente = Docente.objects.get(id=docente_id)
    orientandos = docente.orientandos.all()
    return render(request, "relatorios/docente.html", {
        "docente": docente,
        "orientandos": orientandos
    })

def homepage(request):
    return render(request, "relatorios/home.html")

def lista_aluno(request):
    return render(request, "relatorios/lista_aluno.html", {
        "alunos": Aluno.objects.all()
    })

def aluno(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    return render(request, "relatorios/aluno.html", {
        "aluno": aluno
    })

def lista_relatorio(request):
    relatorios = Relatorio.objects.all().order_by("-periodo", "aluno")
    return render(request, "relatorios/lista_relatorio.html", {
        "relatorios": relatorios,
    })
