from rest_framework import viewsets
from ..models import AlgumaCoisa
from .serializers import AlgumaCoisaSerializer

class AlgumaCoisaViewSet(viewsets.ModelViewSet):
    queryset = AlgumaCoisa.objects.all()
    serializer_class = AlgumaCoisaSerializer