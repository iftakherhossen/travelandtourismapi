from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    
    class Meta:
        model = Blog
        fields = '__all__'