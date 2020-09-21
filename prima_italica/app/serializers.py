from rest_framework import serializers

from prima_italica.app import models


class VoluntarioSerializer(serializers.ModelSerializer):
    """Serializer for Voluntario"""

    class Meta:
        model = models.Voluntario
        fields = (
            'id',
            'nome',
            'sobrenome',
            'bairro',
            'cidade'
        )


class AcaoSerializer(serializers.ModelSerializer):
    """Serializer for Voluntario"""

    class Meta:
        model = models.Acao
        fields = (
            'id',
            'nome_acao',
            'instituicao_organizadora',
            'endereco',
            'bairro',
            'cidade',
            'descricao',
        )
