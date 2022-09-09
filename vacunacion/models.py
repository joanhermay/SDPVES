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
    nombres = models.CharField(max_length=100, null=False, default='--')
    apellidos = models.CharField(max_length=100, null=False, default='--')
    departamento_de_nacimiento = models.ForeignKey(Departamento, on_delete=models.CASCADE,
                                                   to_field='codigo_departamento')
    municipio_de_nacimiento = models.ForeignKey(Municipio, on_delete=models.CASCADE)
