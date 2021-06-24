from django.db import models


# Create your models here.


class Departamento(models.Model):
    codigo_departamento = models.CharField(max_length=2, null=False, default='--', blank=False)
    nombre = models.CharField(max_length=100, null=False, default='--', blank=False)


class Municipio(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False, default='--')
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)


class Persona(models.Model):
    nombres = models.CharField(max_length=100, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    dui = models.CharField(max_length=10, null=False, blank=False, unique=True)
    fecha_de_nacimiento = models.DateField(blank=False, null=False)
    departamento_de_nacimiento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, to_field='id')
    municipio_de_nacimiento = models.ForeignKey(Municipio, on_delete=models.SET_NULL, null=True, to_field='id')
