# forms.py
import bcrypt
from django import forms
from django.contrib.auth.models import User

from django_countries.fields import CountryField
from . import models
from .models import City



class WeatherForm(forms.ModelForm):
    country = CountryField().formfield(required=False)
    city_name = forms.CharField(max_length=255)

    class Meta:
        model = models.WeatherData  # Specify the model
        fields = ['country', 'city_name']

    def clean_country(self):
        country = self.cleaned_data['country']
        if not country:
            raise forms.ValidationError('Please Select A Country')
        return country


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)




class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']

