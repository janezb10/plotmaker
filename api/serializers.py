from rest_framework import serializers
from .models import Scatter

class ScatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scatter
        fields = ['id', 'x', 'y']