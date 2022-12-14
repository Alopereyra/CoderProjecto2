"""CoderProjecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from AppCoder2.views import entregables, estudiantes, inicio, cursos, profesores, ayuda


urlpatterns = [
    path("inicio/", inicio, name="inicio"),
    path("entregables/", entregables, name="entregables"),
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("cursos/", cursos, name="mis_cursos"),
    path("profesores/", profesores, name="profesores"),
    path("ayuda/", ayuda),
    
]