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
        fields = (
        			'name', 'donator',  'category', 'qty',
        			'added_at', 'expiry', 'address', 'photo', 'tag',
    			  )
      
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)
        self.fields['donator'].widget.attrs['hidden'] = 'True'
        self.fields['donator'].label = False



# class FoodForm(ModelForm):
#     added_at = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
#     expiry = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
#     class Meta:
#         model = Food
#         # fields = '__all__'
#         fields = (
#         			'name', 'donator', 'food_type', 'category', 'qty',
#         			'added_at', 'expiry', 'address', 'photo', 'tag',
#     			  )

#         widgets = {
#         			'name': forms.TextInput(attrs = {'class': 'form-control'}),
#         			'donator': forms.TextInput(attrs = {'class': 'form-control'}),
#         			'food_type': forms.TextInput(attrs = {'class': 'form-control'}),
#         			'category': forms.TextInput(attrs = {'class': 'form-control'}),
#         			'qty': forms.TextInput(attrs = {'class': 'form-control'}),
#         			'added_at': forms.TextInput(attrs = {'class': 'form-control'}),
#         			'expiry': forms.TextInput(attrs = {'class': 'form-control'}),
#         			'address': forms.TextInput(attrs = {'class': 'form-control'}),
#         			'photo': forms.TextInput(attrs = {'class': 'form-control'}),
#         			'tag': forms.TextInput(attrs = {'class': 'form-control'}),
#         			}




#     def __init__(self, *args, **kwargs):
#         super(FoodForm, self).__init__(*args, **kwargs)
#         self.fields['donator'].widget.attrs['hidden'] = 'True'
#         self.fields['donator'].label = False