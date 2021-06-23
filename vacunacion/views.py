from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from vacunacion.models import Departamento, Municipio, Persona


def principal(request):
    departametos = Departamento.objects.all()
    municipios = Municipio.objects.all()
    personas = Persona.objects.all()
    total_por_dep = {}

    for dep in departametos:
        total_por_dep[dep.nombre] = personas.filter(departamento_de_nacimiento=dep.id).count()

    total_por_muni = {}
    for muni in municipios:
        total_por_muni[muni.nombre] = personas.filter(municipio_de_nacimiento=muni.id).count()

    context = {'departamentos': departametos,
               'municipios': municipios,
               'personas': personas,
               'total_por_depas': total_por_dep,
               'total_por_munis': total_por_muni}
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


def administrador(request):
    context = {
        'personas': Persona.objects.all()
    }
    return render(request, 'vacunacion/administrador.html', context)


def formulario_registrar_persona_vacunada(request):
    context = {
        'departamentos': Departamento.objects.all(),
        'municipios': Municipio.objects.all(),
    }

    if request.method == 'POST' and request.POST.get("guardar"):
        persona = Persona()
        persona.nombres = request.POST.get("nombres")
        persona.apellidos = request.POST.get("apellidos")
        persona.dui = request.POST.get("dui")
        request.POST.get("dui")
        persona.departamento_de_nacimiento = get_object_or_404(Departamento, id=request.POST.get("departamento"))
        persona.municipio_de_nacimiento = get_object_or_404(Municipio, id=request.POST.get("municipio"))
        persona.fecha_de_nacimiento = request.POST.get("fecha-nacimiento")
        try:
            persona.save()
            context["mensaje"] = "Persona guardada con éxito"
        except Exception as e:
            context["mensaje"] = e.args.__str__()
            context["dui_"] = request.POST.get("dui")

    return render(request, 'vacunacion/guardar_persona.html', context)


def modificar_persona(request, id_persona):
    persona = get_object_or_404(Persona, id=id_persona)
    context = {
        'persona': persona,
        'departamentos': Departamento.objects.all(),
        'municipios': Municipio.objects.all()
    }
    if request.method == 'POST' and request.POST.get("modificar"):
        persona.nombres = request.POST.get("nombres")
        persona.apellidos = request.POST.get("apellidos")
        persona.departamento_de_nacimiento = get_object_or_404(Departamento, id=request.POST.get("departamento"))
        persona.municipio_de_nacimiento = get_object_or_404(Municipio, id=request.POST.get("municipio"))
        persona.fecha_de_nacimiento = request.POST.get("fecha-nacimiento")
        try:
            persona.save()
            context["mensaje"] = "Persona modificada con éxito"
        except Exception as e:
            context["mensaje"] = e.args.__str__()

    return render(request, 'vacunacion/modificar_persona.html', context)


def eliminar_persona(request, id_persona):
    Persona.objects.get(id=id_persona).delete()
    return redirect("administrar-personas-vacunadas")
