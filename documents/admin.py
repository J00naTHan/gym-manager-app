from django.contrib import admin
from .models import Planilha, Avaliacao


@admin.register(Planilha)
class CustomPlanilhaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nome', ('cliente', 'professor')]}),
        ('Exercícios', {'fields': ['exercicios', ('realizada', 'duracao')]}),
        ('Informações Adicionais', {'fields': ['expirada']}),
    ]
    readonly_fields = ['criadaEm', 'atualizadaEm']


@admin.register(Avaliacao)
class CustomAvaliacaoAdmin(admin.ModelAdmin):
    fieldsets = [
        (
            None,
            {
                'fields': [('cliente', 'encarregado'),]
            }
        ),
        (
            'Conteúdo',
            {
                'fields': ['conteudo', 'infoAdicional']
            }
        ),
    ]
    readonly_fields = ['data']
