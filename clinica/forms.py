from django import forms
from .models import Ambulatorio, Convenio, Medico, Paciente, Atende, Consulta, Possui

class AmbulatorioForm(forms.ModelForm):
    class Meta:
        model = Ambulatorio
        fields = '__all__'

class ConvenioForm(forms.ModelForm):
    class Meta:
        model = Convenio
        fields = '__all__'

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class AtendeForm(forms.ModelForm):
    class Meta:
        model = Atende
        fields = '__all__'

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'

class PossuiForm(forms.ModelForm):
    class Meta:
        model = Possui
        fields = '__all__'