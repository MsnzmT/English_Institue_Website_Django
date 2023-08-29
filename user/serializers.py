from rest_framework import serializers
from django.contrib.auth import get_user_model  # If used custom user model
from persiantools.digits import en_to_fa

User = get_user_model()

class PersianIntegerField(serializers.Field):
    def to_representation(self, value):
        return en_to_fa(str(value))

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
    
    phone_number = PersianIntegerField()
    
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name','last_name', 'username', 'sex', 'location', 'phone_number','profile_image')
        
    

class EditUserSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'sex', 'location', 'phone_number','profile_image')
        
        
    def validate_phone_number(self, value):
        if value == None or value == "":
            return value
        if not (value.startswith('۰۹') or value.startswith('09')):
            raise serializers.ValidationError("شماره موبایل شما باید با ۰۹ شروع شود")
        if len(value) != 11 :
            raise serializers.ValidationError("شماره موبایل 11 رقمی است")

        
        return value

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.location = validated_data.get('location', instance.location)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        
        instance.save()
        return instance
        