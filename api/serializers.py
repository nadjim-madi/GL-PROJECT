# serializers.py
from rest_framework import serializers
from lawyer.models import Lawyer

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'
