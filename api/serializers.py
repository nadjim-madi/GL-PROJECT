# serializers.py
from rest_framework import serializers
from lawyer.models import Lawyer
from .models import PrendreRendezVous

class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'


class PrendreRendezVousSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrendreRendezVous
        fields = '__all__'