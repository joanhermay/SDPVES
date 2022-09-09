from django.urls import path

import vacunacion
from . import views

app_name: 'vacunacion'

urlpatterns = [
    path('', views.principal, name="principal"),
    path('administrador/gestion/', views.listar_personas_vacunadas, name='listar-personas-vacunadas'),
    path('administrador/registrar/', views.registrar_persona_vacunada,
         name="registro"),
    path('administrador/modificar/<int:id_persona>/', views.modificar_persona_vacunada,
         name='modificar-persona-vacunada'),

    path('administrador/eliminar/<int:id_persona>#/', views.eliminar_persona_vacunada,
         name='eliminar-persona-vacunada'),
]
