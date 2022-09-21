from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


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
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    cuerpo = RichTextField()
    fecha = models.DateField()
    imagen =  models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo} {self.autor}'

class Comentario(models.Model):
    articulo = models.ForeignKey(Blog, on_delete=models.CASCADE)
    cuerpo = RichTextField()
    autor = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fecha = models.DateField()

    def __str__(self) -> str :
            return f'{self.autor} {self.articulo}'







