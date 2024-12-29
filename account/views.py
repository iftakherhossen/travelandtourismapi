from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer, RegistrationSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Restrict write actions to authenticated users
            permission_classes = [IsAuthenticated]
        else:
            # Allow any user to read data (GET)
            permission_classes = [AllowAny]
        
        return [permission() for permission in permission_classes]
    
class RegistrationApiView(APIView):
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)        
        
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            return Response(f"Account created successfully! Welcome {user.username}")
        return Response(serializer.errors)
    
class LoginApiView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return Response(f"Logged in successfully! Welcome {user.username}")
            else:
                return Response({"error": "Invalid credentials. Please try again."})
            
        return Response(serializer.errors)
    
class LogoutApiView(APIView):
    def get(self, request):
        logout(request)
        return redirect('login')