from django.urls import path
from . import views

urlpatterns = [
    path("docente/", views.lista_docente, name="lista_docente"),
    path("docente/<int:docente_id>", views.docente, name="docente"),
    path("", views.homepage, name="home"),
    path("aluno/", views.lista_aluno, name="lista_aluno"),
    path("aluno/<int:aluno_id>", views.aluno, name="aluno"),
    path("relatorio/", views.lista_relatorio, name="lista_relatorio"),
    path("aluno/<int:aluno_id>/preencher/<int:relatorio_id>", views.preencher, name="preencher"),
]
