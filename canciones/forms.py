from django import forms 
from .models import Cancion

class CancionForm(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = '__all__'
        widgets = {
            'anio_lanzamiento': forms.NumberInput(attrs={'min': 1900}),
            'calificacion': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'duracion': forms.NumberInput(attrs={'min': 1}),
            'reproducciones': forms.NumberInput(attrs={'min': 0}),
        }