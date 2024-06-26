from django import forms
from .models import Ingredients



class IngForm(forms.ModelForm):
    
    class Meta:
        model = Ingredients
        fields = '__all__'






