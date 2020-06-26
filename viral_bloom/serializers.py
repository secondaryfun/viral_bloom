from rest_framework import serializers
from .models import CovidDataByDate


class CovidDataByDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidDataByDate
        fields = ('id', 'date', 'state', 'positive', 'death', 'recovered')
