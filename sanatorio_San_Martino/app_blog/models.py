from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Blog(models.Model):
    titulo = models.CharField(max_length=80)
    subtitulo = models.CharField(max_length=80)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    cuerpo = RichTextField()
    fecha = models.DateField(auto_now=True)
    imagen =  models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return f'Entrada: {self.titulo}-{self.autor}'

class Comentario(models.Model):
    articulo = models.ForeignKey(Blog, on_delete=models.CASCADE)
    cuerpo = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=True)

    def __str__(self) -> str :
            return f'Comentario por : {self.autor}'
