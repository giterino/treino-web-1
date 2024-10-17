from django.shortcuts import render
from .models import Docente

# Create your views here.

def lista_docente(request):
    return render(request, "relatorios/lista_docente.html", {
        "docentes": Docente.objects.all()
    })
