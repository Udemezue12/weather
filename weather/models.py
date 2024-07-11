import uuid
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField, countries



    
    # country = models.CharField(max_length=255, null=True, choices=COUNTRY_CHOICES)
    # other fields...

    
# Create your models here.

class WeatherData(models.Model):
    COUNTRY_CHOICES = list(countries)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    wind_speed = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=255, null=True, choices=COUNTRY_CHOICES)

    weather_data_id= models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def __str__(self) -> str:
        return f"{self.user} - {self.country}, {self.timestamp}"
    
    def __str__(self):
        return self.get_country_display() if self.country else 'Unknown Country'
    
class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

