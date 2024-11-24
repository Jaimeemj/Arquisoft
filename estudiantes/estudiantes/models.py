from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    correo = models.EmailField()
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre + ' ' + self.apellido

# Create your models here.
