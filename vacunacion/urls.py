from django.urls import path

import vacunacion
from . import views

app_name: 'vacunacion'
urlpatterns = [
    path('', views.principal),
    path('municipio/<str:codigo_depa>', views.mostrar_municipios, name='mostrar_municipios'),
    path('ingresar_persona_vacunada', views.registrar_a_persona_vacunada, name="ingresar_persona_vacunada"),
    path('departamentos', views.mostrar_departamentos, name='mostrar_departamentos')
]
