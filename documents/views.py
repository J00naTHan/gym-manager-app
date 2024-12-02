from django.shortcuts import render
from rest_framework import viewsets

from documents.models import Planilha, Avaliacao
from documents.serializers import PlanilhaSerializer, AvaliacaoSerializer


class PlanilhaViewSet(viewsets.ModelViewSet):
    queryset = Planilha.objects.all()
    serializer_class = PlanilhaSerializer
    permission_classes = []


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    permission_classes = []
