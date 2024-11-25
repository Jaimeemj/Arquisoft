from django.db import models

class Cobro(models.Model):
    estudiante = models.IntegerField(null=False, default=None)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Cobro de {self.monto}"
    

# Create your models here.
