from django.db import models
from constant import STAR_CHOICES

# Create your models here.
class Review(models.Model):
    image = models.ImageField(upload_to='media_uploads/teams/')
    name = models.CharField(max_length=100)
    content = models.TextField()
    ratings = models.CharField(max_length=10, choices=STAR_CHOICES)
    
    def __str__(self):
        return f"{self.content} Reviewed by - {self.name}"