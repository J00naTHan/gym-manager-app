from rest_framework import serializers
from .models import Planilha, Avaliacao


class PlanilhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planilha
        fields = "__all__"


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = "__all__"
