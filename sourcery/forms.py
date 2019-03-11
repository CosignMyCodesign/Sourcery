from django.contrib.auth.models import User
from django import forms
from sourcery.models import Resource_Type
# from sourcery.models import Product

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class Resource_Type_Form(forms.ModelForm):

    class Meta:
        model = Resource_Type
        fields = ('name',)
