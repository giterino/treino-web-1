from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms

from .models import Docente, Aluno, Relatorio, Avaliacao

from .utils import obtem_periodo_atual

class FormularioRelatorio(forms.Form):
    opcoes_artigo = [
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3", "3 ou mais"),
    ]
    rotulo_artigos = "Artigos aceitos ou publicados"
    nro_artigos_aceitos = forms.ChoiceField(
        label=rotulo_artigos,
        choices=opcoes_artigo,
    )
    rotulo_atividades_academicas = "Relato das atividades acadêmicas"
    atividades_academicas = forms.CharField(
        label=rotulo_atividades_academicas,
        widget=forms.Textarea,
    )
    rotulo_atividades_pesquisa = "Relato das atividades de pesquisa"
    atividades_pesquisa = forms.CharField(
        label=rotulo_atividades_pesquisa,
        widget=forms.Textarea,
    )

class FormularioAvaliacao(forms.Form):
    rotulo_parecer = "Parecer"
    parecer = forms.CharField(
        label=rotulo_parecer,
        widget=forms.Textarea,
    )
    rotulo_conceito = "Conceito"
    conceito = forms.ChoiceField(
        label=rotulo_conceito,
        choices=Avaliacao.Conceito.choices,
    )

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
    periodo_atual = obtem_periodo_atual()
    relatorio_atual = Relatorio.objects.filter(
        aluno=aluno,
        periodo=periodo_atual,
    ).first()
    return render(request, "relatorios/aluno.html", {
        "aluno": aluno,
        "relatorio_atual": relatorio_atual,
    })

def lista_relatorio(request):
    relatorios = Relatorio.objects.all().order_by("-periodo", "aluno")
    return render(request, "relatorios/lista_relatorio.html", {
        "relatorios": relatorios,
    })

def preencher(request, aluno_id, relatorio_id):
    aluno = Aluno.objects.get(id=aluno_id)
    relatorio = Relatorio.objects.get(id=relatorio_id)
    docente = relatorio.docente_responsavel
    if request.method == "POST":
        form = FormularioRelatorio(request.POST)
        if form.is_valid():
            relatorio.nro_artigos_aceitos = form.cleaned_data["nro_artigos_aceitos"]
            relatorio.atividades_academicas = form.cleaned_data["atividades_academicas"]
            relatorio.atividades_pesquisa = form.cleaned_data["atividades_pesquisa"]
            relatorio.status = Relatorio.Status.PREENCHIDO
            relatorio.save()
            return redirect(reverse("aluno", args=[aluno_id]))
    else:
        form = FormularioRelatorio()

    return render(request, "relatorios/submissao.html", {
        "aluno": aluno,
        "relatorio": relatorio,
        "docente": docente,
        "form": form,
    })

def relatorio(request, relatorio_id):
    relatorio = Relatorio.objects.get(id=relatorio_id)
    return render(request, "relatorios/relatorio.html", {
        "relatorio": relatorio,
    })

def avaliar(request, relatorio_id):
    relatorio = Relatorio.objects.get(id=relatorio_id)
    form = FormularioAvaliacao()
    contexto = {
        "relatorio": relatorio,
        "form": form,
    }
    return render(request, "relatorios/submissao_avaliacao.html", contexto)

