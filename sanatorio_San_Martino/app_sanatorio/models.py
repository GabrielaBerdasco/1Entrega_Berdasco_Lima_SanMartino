from django.db import models

class Medico(models.Model):

    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    especialidad = models.CharField(max_length=80)
    email = models.EmailField()


class Paciente(models.Model):
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    fecha_nacimiento = models.DateField()
    ciudad = models.CharField(max_length=80)
    telefono = models.IntegerField()
    email = models.EmailField()


class ObrasSociales(models.Model):
    nombre = models.CharField(max_length=80)
    telefono = models.IntegerField()
    email = models.EmailField()
