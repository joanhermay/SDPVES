# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register(Departamento),
admin.site.register(Municipio),
admin.site.register(Persona)
