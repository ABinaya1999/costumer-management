from django import forms
from .models import Record

class addrecord(forms.ModelForm):
    first_name=forms.CharField(label='first_name',widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(label='last_name',widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(label='email',widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(label='address',widget=forms.TextInput(attrs={'class':'form-control'}))
    profile_imagee=forms.ImageField(label='profile_image')
    
    class Meta:
        model= Record
        fields = ('first_name','last_name','email','address','profile_imagee')