from django.urls import path
from . import views

urlpatterns = [
    path("docente/", views.lista_docente, name="lista_docente"),
]