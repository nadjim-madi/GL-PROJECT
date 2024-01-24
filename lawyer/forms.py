# forms.py

from django import forms
from .models import Lawyer

class LawyerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Lawyer
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'specialization',
            'password',
            'address',
            'DOB',

        ]
        
