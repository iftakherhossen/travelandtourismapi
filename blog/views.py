from django.shortcuts import render
from rest_framework import viewsets
from .models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Restrict write actions to authenticated users
            permission_classes = [IsAuthenticated]
        else:
            # Allow any user to read data (GET)
            permission_classes = [AllowAny]
        
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.request.query_params.get('slug', None)

        if slug:
            queryset = queryset.filter(slug=slug)

        return queryset
