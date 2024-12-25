from django.db import models
from team.models import Team
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    operator = models.OneToOneField(Team, on_delete=models.CASCADE, related_name='account')
    created_on = models.DateField(auto_now_add=True)
        
    def __str__(self):
        return f"{self.user.username}"