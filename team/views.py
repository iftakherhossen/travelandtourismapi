from django.shortcuts import render
from rest_framework import viewsets
from .models import Team
from .serializers import TeamSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    
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
        username = self.request.query_params.get('username', None)
        name = self.request.query_params.get('name', None)

        if username:
            queryset = queryset.filter(username=username)
        if name:
            queryset = queryset.filter(name=name)

        return queryset