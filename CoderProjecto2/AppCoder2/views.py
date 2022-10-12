from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def mostrar_inicio(request):
    return render(request, "AppCoder2/inicio.html",)


def cursos(request):
    return render(request, "AppCoder2/cursos.html")


def profesores(request):
    return render(request, "AppCoder2/profesores.html")


def estudiantes(request):
    return render(request, "AppCoder2/estudiantes.html")


def entregables(request):
    return render(request, "AppCoder2/entregables.html")

