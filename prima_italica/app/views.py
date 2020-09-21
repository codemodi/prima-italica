from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from prima_italica.app import serializers, models


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


class VoluntarioViewSet(viewsets.ModelViewSet):
    """Handles CRUD"""
    serializer_class = serializers.VoluntarioSerializer
    queryset = models.Voluntario.objects.all()


class AcaoViewSet(viewsets.ModelViewSet):
    """Handles CRUD"""
    serializer_class = serializers.AcaoSerializer
    queryset = models.Acao.objects.all()
