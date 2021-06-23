from django.db import models


# Create your models here.


class Departamento(models.Model):
    codigo_departamento = models.CharField(max_length=2, null=False, default='--', unique=True)
    nombre = models.CharField(max_length=100, null=False, default='--')

    def __str__(self):
        return self.nombre


class Municipio(models.Model):
    nombre = models.CharField(max_length=100, null=False, default='--')
    codigo_departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, to_field='codigo_departamento')

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    id = models.BigAutoField(primary_key=True)
    departamento_de_nacimiento = models.ForeignKey(Departamento, models.DO_NOTHING)
    municipio_de_nacimiento = models.ForeignKey(Municipio, models.DO_NOTHING)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    dui = models.CharField(max_length=10, null=False, blank=False, unique=True)
    fecha_de_nacimiento = models.DateField(blank=False, null=False)
    nombres = models.CharField(max_length=100, null=False, blank=False)
