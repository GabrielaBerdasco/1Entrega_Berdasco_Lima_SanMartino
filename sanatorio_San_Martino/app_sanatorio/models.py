from django.db import models
from django.contrib.auth.models import User


class Medico(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    especialidad = models.CharField(max_length=80)
    email = models.EmailField()

    def __str__(self) -> str :
            return f'{self.nombre} {self.apellido}'


class Blog(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=80)
    autor = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    cuerpo = models.TextField()
    fecha = models.DateField()
    imagen =  models.ImageField(upload_to='imagenes', null=True, blank = True)




