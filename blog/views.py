from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.
class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.request.query_params.get('slug', None)

        if slug:
            queryset = queryset.filter(slug=slug)