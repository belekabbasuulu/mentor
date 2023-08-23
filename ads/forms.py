from django import forms

from .models import Ads


class AdForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = '__all__'
    
