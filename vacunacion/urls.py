from django.urls import path

import vacunacion
from . import views

app_name: 'vacunacion'

urlpatterns = [
    path('', views.principal, name="pagina-principal"),
    path('administrar_personas', views.administrador, name='administrar-personas-vacunadas'),
    path('registrar_personas', views.formulario_registrar_persona_vacunada,
         name="registro"),
    path('modificar_persona/<int:id_persona>', views.modificar_persona, name='modificar-persona-vacunada'),

    path('eliminar_persona/<int:id_persona>', views.eliminar_persona, name='eliminar-persona-vacunada'),
    # path('departamentos', views.mostrar_departamentos, name='departamentos'),
    # path('municipio/<str:codigo_depa>', views.mostrar_municipios, name='municipios'),
]
