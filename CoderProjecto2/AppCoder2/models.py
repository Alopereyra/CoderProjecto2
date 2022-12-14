from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()
    fecha_de_inicio = models.DateField(null=True)

    def __str__(self):
        return f"({self.camada}) {self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"

class Entergable(models.Model):
    nombre = models.CharField(max_length=30)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.fecha_de_entrega}"