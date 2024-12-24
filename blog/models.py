from django.db import models
from team.models import Team

# Create your models here.
class Blog(models.Model):
    image = models.ImageField(upload_to='media_uploads/blogs/', blank=True, null=True)
    title = models.CharField(max_length=350)
    slug = models.SlugField(unique=True, max_length=350)
    content = models.TextField()
    author = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='blogs')
    created_on = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_on']
        
    def __str__(self):
        return f"{self.title} by {self.author}"