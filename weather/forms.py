# forms.py
import bcrypt
import re
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model as user_model
from django.core.exceptions import ValidationError

from django_countries.fields import CountryField
from . import models
from .models import City


User = user_model()


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)
    email = forms.EmailField(
        help_text='A valid email address, please.', required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('The email has already been registered')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if (len(password) < 8 or not re.search(r'[A-Z]', password) or
            not re.search(r'[a-z]', password) or not re.search(r'\d', password) or
                not re.search(r'[!@#$%^&*(),.?":{}|<>]', password)):
            raise ValidationError(
                'Password must be at least 8 characters long, contain at least one uppercase letter, '
                'one lowercase letter, one digit, and one special character'
            )
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password != password2:
            raise ValidationError("Passwords do not match.")

        self.clean_password()  # Ensure password requirements are met

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


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


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
