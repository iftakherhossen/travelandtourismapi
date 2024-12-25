from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Account
from .serializers import AccountSerializer, RegistrationSerializer, LoginSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Create your views here.
class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
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