from django import forms
from .models import Inscrito, Institucion

class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = '__all__'

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = '__all__'
        widgets = {
            'estado': forms.Select(attrs={'class': 'form-control'}),}