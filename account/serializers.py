from rest_framework import serializers
from .models import Account
from team.models import Team
from django.contrib.auth.models import User

class AccountSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    operator = serializers.StringRelatedField(many=False)
    
    class Meta:
        model = Account
        fields = '__all__'
        
class RegistrationSerializer(serializers.ModelSerializer):
    operator = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), required=True)
    confirm_password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'operator']
                
    def save(self):
        username = self.validated_data['username']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        operator = self.validated_data['operator']
        
        if password != confirm_password:
            raise serializers.ValidationError({"error": "Password doesn't matched"})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"error": "You can't choose this username, it already exists."})
        
        user = User(username=username)
        user.set_password(password)
        user.email = operator.email
        user.save()
        
        Account.objects.create(
            user = user,
            operator = operator
        )
        
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)