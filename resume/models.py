from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='resume/', null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    education = models.CharField(max_length=100)
    experience = models.TextField()
    skills = models.TextField()
    portfolio = models.URLField(null=True, blank=True)
    city = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE')
    )
    gender = models.CharField(max_length=10, choices=GENDER)

    def __str__(self):
        return self.username