from django.db import models



class Lawyer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=128)
    address = models.CharField(max_length=255)
    DOB = models.DateField(max_length=255)
    rating = models.IntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'lawyers'
