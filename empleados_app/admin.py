from django.contrib import admin
from .models import Rol, Empleado, HistorialDeAcceso, RegistroDeAsistencia

admin.site.register(Rol)
admin.site.register(Empleado)
admin.site.register(HistorialDeAcceso)
admin.site.register(RegistroDeAsistencia)

