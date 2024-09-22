from rest_framework import serializers
from .models import FloatData, BooleanData

class FloatDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloatData
        fields = ['todayUsage', 'monthUsage', 'device1Usage', 'device2Usage', 'device3Usage']

class BooleanDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooleanData
        fields = ['device1Switch', 'device2Switch', 'device3Switch']
