from django.shortcuts import render

from AppCoder2.models import Estudiante


# Create your views here.

def ayuda(request):
    return render(request, "AppCoder2/ayuda.html")

def inicio(request):
    estudiante = Estudiante(nombre="Eduardo", apellido="Lopez", email="edu@ar.com")
    
    contexto = {"estudiante1": estudiante}
    return render(request, "AppCoder2/inicio.html",contexto)


def cursos(request):
    
    return render(request, "AppCoder2/cursos.html")


def profesores(request):
    return render(request, "AppCoder2/profesores.html")


def estudiantes(request):
    return render(request, "AppCoder2/estudiantes.html")


def entregables(request):
    return render(request, "AppCoder2/entregables.html")

