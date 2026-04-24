from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from clinica.models import Ambulatorio, Convenio, Medico, Paciente, Atende, Consulta, Possui
