"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clinica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    
    # AMBULATÓRIO
    path('ambulatorios/', views.ambulatorio_list, name='ambulatorio_list'),
    path('ambulatorios/novo/', views.ambulatorio_create, name='ambulatorio_create'),
    path('ambulatorios/editar/<int:id>/', views.ambulatorio_update, name='ambulatorio_update'),
    path('ambulatorios/deletar/<int:id>/', views.ambulatorio_delete, name='ambulatorio_delete'),
    
    # CONVÊNIO
    path('convenios/', views.convenio_list, name='convenio_list'),
    path('convenios/novo/', views.convenio_create, name='convenio_create'),
    path('convenios/editar/<int:codconv>/', views.convenio_update, name='convenio_update'),
    path('convenios/deletar/<int:codconv>/', views.convenio_delete, name='convenio_delete'),
    
    # MÉDICO
    path('medicos/', views.medico_list, name='medico_list'),
    path('medicos/novo/', views.medico_create, name='medico_create'),
    path('medicos/editar/<int:crm>/', views.medico_update, name='medico_update'),
    path('medicos/deletar/<int:crm>/', views.medico_delete, name='medico_delete'),
    
    # PACIENTE
    path('pacientes/', views.paciente_list, name='paciente_list'),
    path('pacientes/novo/', views.paciente_create, name='paciente_create'),
    path('pacientes/editar/<int:id>/', views.paciente_update, name='paciente_update'),
    path('pacientes/deletar/<int:id>/', views.paciente_delete, name='paciente_delete'),
    
    # ATENDE
    path('atende/', views.atende_list, name='atende_list'),
    path('atende/novo/', views.atende_create, name='atende_create'),
    path('atende/editar/<int:id>/', views.atende_update, name='atende_update'),
    path('atende/deletar/<int:id>/', views.atende_delete, name='atende_delete'),
    
    # CONSULTA
    path('consultas/', views.consulta_list, name='consulta_list'),
    path('consultas/novo/', views.consulta_create, name='consulta_create'),
    path('consultas/editar/<int:id>/', views.consulta_update, name='consulta_update'),
    path('consultas/deletar/<int:id>/', views.consulta_delete, name='consulta_delete'),
    
    # POSSUI
    path('possui/', views.possui_list, name='possui_list'),
    path('possui/novo/', views.possui_create, name='possui_create'),
    path('possui/editar/<int:id>/', views.possui_update, name='possui_update'),
    path('possui/deletar/<int:id>/', views.possui_delete, name='possui_delete'),
    
    # GRÁFICO
    path('grafico/pacientes-ambulatorio/', views.grafico_pacientes_ambulatorio, name='grafico_pacientes'),
]
