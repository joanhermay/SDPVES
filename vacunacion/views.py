from django.shortcuts import render

# Create your views here.
from vacunacion.models import Departamento, Municipio


def principal(request):
    context = {'departamentos': Departamento.objects.all(),
               'municipios': Municipio.objects.all()}
    return render(request, 'vacunacion/principal.html', context)


def mostrar_municipios(request, codigo_depa):
    municipios_dep = Municipio.objects.filter(codigo_departamento=codigo_depa)
    nom_dep = Departamento.objects.get(codigo_departamento=codigo_depa).nombre
    context = {'munis': municipios_dep,
               'nombre_dep': nom_dep}
    return render(request, 'vacunacion/mostrar_municipios.html', context)


def mostrar_departamentos(request):
    departamentos = Departamento.objects.all()
    municipios = Municipio.objects.all()
    context = {
        'departamentos': departamentos,
        'municipios': municipios,
    }
    return render(request, 'vacunacion/mostrar_departamentos.html', context)


def registrar_a_persona_vacunada(request):
    context = {
        'departamentos': Departamento.objects.all(),
        'municipios': Municipio.objects.all()
    }
    return render(request, 'vacunacion/registrar_a_persona_vacunada.html', context)
