from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from clinica.models import Ambulatorio, Convenio, Medico, Paciente, Atende, Consulta, Possui
from django.db.models import Count
from clinica.forms import AmbulatorioForm, ConvenioForm, MedicoForm, PacienteForm, AtendeForm, ConsultaForm, PossuiForm
from django.views.generic import TemplateView


# ==================== AMBULATÓRIO ====================

def ambulatorio_list(request):
    ambulatorios = Ambulatorio.objects.all()
    return render(request, 'clinica/ambulatorio_list.html', 
                  {'ambulatorios':ambulatorios})

def ambulatorio_create(request):
    if request.method == 'POST':
        form = AmbulatorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ambulatorio_list')
    else:
        form = AmbulatorioForm()
    return render(request, 'clinica/ambulatorio_form.html', {'form': form})

def ambulatorio_update(request, id):
    ambulatorio = get_object_or_404(Ambulatorio, pk=id)
    if request.method == 'POST':
        form = AmbulatorioForm(request.POST, instance=ambulatorio)
        if form.is_valid():
            form.save()
            return redirect('ambulatorio_list')
    else:
        form = AmbulatorioForm(instance=ambulatorio)
    return render(request, 'clinica/ambulatorio_form.html', {'form': form})

def ambulatorio_delete(request, id):
    ambulatorio = get_object_or_404(Ambulatorio, pk=id)
    if request.method == 'POST':
        ambulatorio.delete()
        return redirect('ambulatorio_list')
    return render(request, 'clinica/ambulatorio_confirm_delete.html', {'ambulatorio': ambulatorio})

# ==================== CONVÊNIO ====================

def convenio_list(request):
    convenios = Convenio.objects.all()
    return render(request, 'clinica/convenio_list.html', {'convenios': convenios})

def convenio_create(request):
    if request.method == 'POST':
        form = ConvenioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('convenio_list')
    else:
        form = ConvenioForm()
    return render(request, 'clinica/convenio_form.html', {'form': form})

def convenio_update(request, codconv):
    convenio = get_object_or_404(Convenio, pk=codconv)
    if request.method == 'POST':
        form = ConvenioForm(request.POST, instance=convenio)
        if form.is_valid():
            form.save()
            return redirect('convenio_list')
    else:
        form = ConvenioForm(instance=convenio)
    return render(request, 'clinica/convenio_form.html', {'form': form})

def convenio_delete(request, codconv):
    convenio = get_object_or_404(Convenio, pk=codconv)
    if request.method == 'POST':
        convenio.delete()
        return redirect('convenio_list')
    return render(request, 'clinica/convenio_confirm_delete.html', {'convenio': convenio})

# ==================== MÉDICO ====================

def medico_list(request):
    medicos = Medico.objects.all()
    return render(request, 'clinica/medico_list.html', {'medicos': medicos})

def medico_create(request):
    if request.method == 'POST':
        form = MedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm()
    return render(request, 'clinica/medico_form.html', {'form': form})

def medico_update(request, crm):
    medico = get_object_or_404(Medico, pk=crm)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
        if form.is_valid():
            form.save()
            return redirect('medico_list')
    else:
        form = MedicoForm(instance=medico)
    return render(request, 'clinica/medico_form.html', {'form': form})

def medico_delete(request, crm):
    medico = get_object_or_404(Medico, pk=crm)
    if request.method == 'POST':
        medico.delete()
        return redirect('medico_list')
    return render(request, 'clinica/medico_confirm_delete.html', {'medico': medico})

# ==================== PACIENTE ====================

def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'clinica/paciente_list.html', {'pacientes': pacientes})

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'clinica/paciente_form.html', {'form': form})

def paciente_update(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'clinica/paciente_form.html', {'form': form})

def paciente_delete(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('paciente_list')
    return render(request, 'clinica/paciente_confirm_delete.html', {'paciente': paciente})

# ==================== ATENDE ====================

def atende_list(request):
    atende = Atende.objects.all()
    return render(request, 'clinica/atende_list.html', {'atende': atende})

def atende_create(request):
    if request.method == 'POST':
        form = AtendeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('atende_list')
    else:
        form = AtendeForm()
    return render(request, 'clinica/atende_form.html', {'form': form})

def atende_update(request, id):
    atende_obj = get_object_or_404(Atende, pk=id)
    if request.method == 'POST':
        form = AtendeForm(request.POST, instance=atende_obj)
        if form.is_valid():
            form.save()
            return redirect('atende_list')
    else:
        form = AtendeForm(instance=atende_obj)
    return render(request, 'clinica/atende_form.html', {'form': form})

def atende_delete(request, id):
    atende_obj = get_object_or_404(Atende, pk=id)
    if request.method == 'POST':
        atende_obj.delete()
        return redirect('atende_list')
    return render(request, 'clinica/atende_confirm_delete.html', {'atende': atende_obj})

# ==================== CONSULTA ====================

def consulta_list(request):
    consultas = Consulta.objects.all()
    return render(request, 'clinica/consulta_list.html', {'consultas': consultas})

def consulta_create(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consulta_list')
    else:
        form = ConsultaForm()
    return render(request, 'clinica/consulta_form.html', {'form': form})

def consulta_update(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('consulta_list')
    else:
        form = ConsultaForm(instance=consulta)
    return render(request, 'clinica/consulta_form.html', {'form': form})

def consulta_delete(request, id):
    consulta = get_object_or_404(Consulta, pk=id)
    if request.method == 'POST':
        consulta.delete()
        return redirect('consulta_list')
    return render(request, 'clinica/consulta_confirm_delete.html', {'consulta': consulta})

# ==================== POSSUI ====================

def possui_list(request):
    possui = Possui.objects.all()
    return render(request, 'clinica/possui_list.html', {'possui': possui})

def possui_create(request):
    if request.method == 'POST':
        form = PossuiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('possui_list')
    else:
        form = PossuiForm()
    return render(request, 'clinica/possui_form.html', {'form': form})

def possui_update(request, id):
    possui_obj = get_object_or_404(Possui, pk=id)
    if request.method == 'POST':
        form = PossuiForm(request.POST, instance=possui_obj)
        if form.is_valid():
            form.save()
            return redirect('possui_list')
    else:
        form = PossuiForm(instance=possui_obj)
    return render(request, 'clinica/possui_form.html', {'form': form})

def possui_delete(request, id):
    possui_obj = get_object_or_404(Possui, pk=id)
    if request.method == 'POST':
        possui_obj.delete()
        return redirect('possui_list')
    return render(request, 'clinica/possui_confirm_delete.html', {'possui': possui_obj})

# ==================== GRÁFICO ====================

def grafico_pacientes_ambulatorio(request):
    from django.db.models import Count
    
    dados = Ambulatorio.objects.annotate(
        pacientes=Count('paciente')
    ).values('nome', 'pacientes')
    
    dados_formatado = [
        {'amb': d['nome'], 'pacientes': d['pacientes']}
        for d in dados
    ]
    
    return render(request, 'clinica/grafico_pacientes.html', {'dados': dados_formatado})

from django.db.models import Count
from django.db.models.functions import ExtractMonth
from .models import Possui, Consulta, Medico, Ambulatorio, Paciente

def index(request):
    dados_convenio = Possui.objects.values('convenio__nome').annotate(total=Count('paciente'))
    labels_convenios = [d['convenio__nome'] for d in dados_convenio]
    dados_pacientes = [d['total'] for d in dados_convenio]
    
    dados_consultas = Consulta.objects.annotate(
        mes=ExtractMonth('data')
    ).values('mes').annotate(
        total=Count('id')
    ).order_by('mes')
    
    meses_abreviados = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    labels_consultas = []
    dados_consultas_qtd = []
    
    for d in dados_consultas:
        mes_num = d['mes']
        if mes_num:
            labels_consultas.append(meses_abreviados[mes_num - 1])
            dados_consultas_qtd.append(d['total'])
            
    dados_especialidades = Medico.objects.values('especialidade').annotate(total=Count('crm'))
    labels_especialidades = [d['especialidade'] if d['especialidade'] else 'Não Informada' for d in dados_especialidades]
    dados_medicos_especialidade = [d['total'] for d in dados_especialidades]
    
    context = {
        'labels_convenios': labels_convenios,
        'dados_pacientes': dados_pacientes,
        'labels_consultas': labels_consultas,
        'dados_consultas_qtd': dados_consultas_qtd,
        'labels_especialidades': labels_especialidades,
        'dados_medicos_especialidade': dados_medicos_especialidade,
    }
    
    return render(request, 'clinica/index.html', context)


class PacientesPorAmbulatorio(TemplateView):
    template_name = 'clinica/index.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        ambulat = Ambulatorio.objects.all()
        dados = []
        for a in ambulat:
            dados.append({
                'ambulatorio': a.nome,
                'pacientes': (Paciente.objects.filter(idamb=a)).count()
            })
        contexto['dados'] = dados
        return contexto
