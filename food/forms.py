from django.forms import widgets
from accounts.models import Donator
from .models import Food
from django.forms import ModelForm
from django import forms
from smart_selects.form_fields import ChainedSelect

class FoodForm(ModelForm):
    added_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    expiry = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    
    class Meta:
        model = Food
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.fields['donator'].widget.attrs['hidden'] = 'True'
        self.fields['donator'].label = False