from django import forms
from .models import Familia, Miembro

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = ['apellido']

class MiembroForm(forms.ModelForm):
    class Meta:
        model = Miembro
        fields = ['nombre', 'edad']
