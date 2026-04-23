from django.contrib import admin
from .models import Ambulatorio, Atende, Consulta, Convenio, Medico, Paciente, Possui

# Register your models here.
admin.site.register(Ambulatorio)
admin.site.register(Atende)
admin.site.register(Consulta)
admin.site.register(Convenio)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Possui)