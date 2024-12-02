from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from documents.models import Planilha, Avaliacao
from documents.serializers import PlanilhaSerializer, AvaliacaoSerializer, SendPlanilhaSerializer


class PlanilhaViewSet(viewsets.ModelViewSet):
    queryset = Planilha.objects.all()
    serializer_class = PlanilhaSerializer

    @action(detail=True, methods=['get'], url_name='print')
    def print_planilha(self, request, pk=None):
        planilha = self.get_object()
        serializer = SendPlanilhaSerializer(planilha)
        return Response(serializer.data)



class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
