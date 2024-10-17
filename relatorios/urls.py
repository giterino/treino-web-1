from django.urls import path
from . import views

urlpatterns = [
    path("docente/", views.lista_docente, name="lista_docente"),
    path("docente/<int:docente_id>", views.docente, name="docente"),
    path("", views.homepage, name="home"),
]
