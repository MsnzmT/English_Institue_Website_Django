from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model



class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'username','password', 'confirm_password')
        
        
    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError('رمز عبور های وارد شده یکسان نیستند')
        return data
    
    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name','last_name', 'username', 'sex', 'location', 'phone_number','profile_image')
        
    

class EditUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'sex', 'location', 'phone_number','profile_image')