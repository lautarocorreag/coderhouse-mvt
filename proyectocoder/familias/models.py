from django.db import models

# Create your models here.

class Familia(models.Model):
    apellido = models.CharField(max_length=50)
    miembros = models.ManyToManyField('Miembro', related_name='familias')

class Miembro(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.PositiveIntegerField()
