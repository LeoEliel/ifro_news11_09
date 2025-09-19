from django.contrib import admin

# Register your models here.
from .models import Cargo, Funcionario

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao']

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargo', 'ativo', 'criado']
    list_editable = ['ativo', '']
