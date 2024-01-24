# core/models.py
from django.db import models
from django.contrib.auth.models import User  # Assuming you are using the built-in User model


from django.db import models

class Lawyer(models.Model):
    lawyer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    DOB = models.DateField(max_length=255)
    class Meta:
        managed = False
        db_table = 'lawyers'
