from django.db import models
from constant import STAR_CHOICES

# Create your models here.
class Team(models.Model):
    image = models.ImageField(upload_to='media_uploads/teams/')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    designation = models.CharField(max_length=200)
    experience = models.CharField(max_length=20)
    ratings = models.CharField(max_length=10, choices=STAR_CHOICES)
    
    def __str__(self):
        return f"{self.name} - {self.designation}"