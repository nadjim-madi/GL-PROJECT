# core/models.py
from django.db import models
from lawyer.models import Lawyer
from django.contrib.auth.models import User  # Assuming you are using the built-in User model


class PrendreRendezVous(models.Model):
    laywer_id = models.ForeignKey(Lawyer, on_delete=models.CASCADE, primary_key=True, db_column='laywer_id')
    id = models.ForeignKey(User, on_delete=models.CASCADE,db_column='user_id')
    rdate = models.DateField()
    situation = models.CharField(max_length=255)

    class Meta:
        db_table = 'prendre_rendez_vous'

