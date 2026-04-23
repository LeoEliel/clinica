# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ambulatorio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    numleitos = models.IntegerField(blank=True, null=True)
    andar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ambulatorio'
    
    def __str__(self):
        return self.nome or f"Ambulatório {self.id}"

class Convenio(models.Model):
    codconv = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'convenio'
    
    def __str__(self):
        return self.nome or f"Convênio {self.codconv}"

class Medico(models.Model):
    crm = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, blank=True, null=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)
    endereco = models.CharField(max_length=250, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    salario = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    idamb = models.ForeignKey(Ambulatorio, models.SET_NULL, db_column='idamb', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico'

    def __str__(self):
        return self.nome or f"CRM: {self.crm}"

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=250, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    idamb = models.ForeignKey(Ambulatorio, models.SET_NULL, db_column='idamb', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paciente'

    def __str__(self):
        return self.nome

class Atende(models.Model):
    id = models.AutoField(primary_key=True)
    medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='medico')
    convenio = models.ForeignKey('Convenio', models.DO_NOTHING, db_column='convenio')

    class Meta:
        managed = False
        db_table = 'atende'
        unique_together = (('medico', 'convenio'),)

    def __str__(self):
        return f"{self.medico} atende {self.convenio}"
    

class Consulta(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateField(blank=True, null=True)
    horario = models.TimeField(blank=True, null=True)
    medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='medico', blank=True, null=True)
    paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='paciente', blank=True, null=True)
    convenio = models.ForeignKey('Convenio', models.DO_NOTHING, db_column='convenio', blank=True, null=True)
    porcent = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'consulta'

    def __str__(self):
        return f"Consulta em {self.data} - {self.medico} para {self.paciente}"
    
class Possui(models.Model):
    id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, models.DO_NOTHING, db_column='paciente')
    convenio = models.ForeignKey(Convenio, models.DO_NOTHING, db_column='convenio')
    tipo = models.CharField(max_length=1, blank=True, null=True)
    vencimento = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'possui'
        unique_together = (('paciente', 'convenio'),)
    def __str__(self):
        return f"{self.paciente} é atendido pelo(a) {self.convenio}"