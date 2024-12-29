from django.shortcuts import render
from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Restrict write actions to authenticated users
            permission_classes = [IsAuthenticated]
        else:
            # Allow any user to read data (GET)
            permission_classes = [AllowAny]
        
        return [permission() for permission in permission_classes]