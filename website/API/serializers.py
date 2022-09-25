from rest_framework import serializers
from ..models import AlgumaCoisa

class AlgumaCoisaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgumaCoisa
        fields = '__all__'