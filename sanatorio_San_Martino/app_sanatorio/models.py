from django.db import models


class Medico(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    especialidad = models.CharField(max_length=80)
    email = models.EmailField()

    def __str__(self) -> str :
            return f'{self.nombre} {self.apellido}'






