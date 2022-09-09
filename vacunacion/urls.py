from django.urls import path

import vacunacion
from . import views

app_name: 'vacunacion'
urlpatterns = [
    path('', views.principal),
    path('municipio/<str:codigo_depa>', views.mostrar_municipios, name='mostrar_municipios'),
    path('departamentos', views.mostrar_departamentos, name='mostrar_departamentos')
]
