from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from vacunacion.models import Departamento, Municipio


def principal(request):
    return render(request, 'vacunacion/principal.html')


def mostrar_municipios(request, codigo_depa):
    municipios_dep = Municipio.objects.filter(codigo_departamento=codigo_depa)
    context = {'munis': municipios_dep,
               'nombre_dep': Departamento.objects.get(codigo_departamento=codigo_depa).nombre}
    return render(request, 'vacunacion/mostrar_municipios.html', context)


def mostrar_departamentos(request):
    departamentos = Departamento.objects.all()
    municipios = Municipio.objects.all()
    context = {
        'departamentos': departamentos,
        'municipios': municipios,
    }
    return render(request, 'vacunacion/mostrar_departamentos.html', context)
