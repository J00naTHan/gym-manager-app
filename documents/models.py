from django.db import models

from users.models import Cliente


class Planilha(models.Model):
    nome = models.CharField(max_length=64)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente_planilha')
    professor = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='professor_planilha')
    exercicios = models.JSONField()
    criadaEm = models.DateTimeField(auto_now_add=True)
    atualizadaEm = models.DateTimeField(auto_now=True)
    duracao = models.IntegerField()
    realizada = models.IntegerField()
    expirada = models.BooleanField()

    def __str__(self):
        return f'{self.nome} ({self.cliente})'


class Avaliacao(models.Model):
    class Meta:
        verbose_name = 'avaliação'
        verbose_name_plural = 'avaliações'

    imagem = models.ImageField(blank=True, null=True, upload_to='uploads/')
    conteudo = models.CharField(blank=True, null=True, max_length=10000)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='cliente_avaliacao')
    encarregado = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='professor_avaliacao')
    infoAdicional = models.CharField(blank=True, null=True, max_length=500)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cliente} - {self.data}'
