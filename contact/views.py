from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Restrict write actions to authenticated users
            permission_classes = [IsAuthenticated]
        else:
            # Allow any user to read data (GET)
            permission_classes = [AllowAny]
        
        return [permission() for permission in permission_classes]