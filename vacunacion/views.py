from django.shortcuts import render

# Create your views here.
from vacunacion.models import Departamento, Municipio


def principal(request):
    municipios = Municipio.objects.all()
    codigos_departamentos = Departamento.objects.all()

    cantidades = []
    nombres_depas = []

    for depa in codigos_departamentos:
        cantidad = 0
        nombres_depas.append(depa.nombre)
        for muni in municipios:
            cd = depa.codigo_departamento
            cm = muni.codigo_departamento.codigo_departamento
            if cd == cm:
                cantidad += 1
        cantidades.append(cantidad)

    context = {'cantidades': cantidades,
               'nombres_depas': nombres_depas}
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
