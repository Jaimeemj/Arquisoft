from django.db import models

from estudiantes.estudiantes.models import Estudiante

class Cobro(models.Model):
    estudiante = models.ForeignKey(Estudiante, related_name='cobros', on_delete=models.CASCADE)
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Cobro de {self.monto} a {self.estudiante.nombre}"
    

# Create your models here.
