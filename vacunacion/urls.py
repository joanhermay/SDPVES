from django.urls import path

import vacunacion
from . import views

app_name: 'vacunacion'
urlpatterns = [
    path('', views.principal),
    path('municipio/<str:codigo_depa>', views.mostrar_municipios, name='municipios'),
    path('registro', views.formulario_registrar_persona_vacunada,
         name="registro"),
    path('departamentos', views.mostrar_departamentos, name='departamentos')
]
