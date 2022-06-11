from rest_framework import serializers
from .models import *
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
from rest_framework.authtoken.models import Token
from django_countries.fields import CountryField
from django.core.validators import RegexValidator
from rest_framework.validators import UniqueTogetherValidator


GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )


class UserProfileSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(
        max_length=68, min_length=2, allow_blank = False, allow_null=False)
    last_name = serializers.CharField(
    max_length=68, min_length=2, allow_blank = False, allow_null=False)
    country_code = CountryField()
    phone_number = serializers.CharField(min_length=11,max_length=11, validators=[RegexValidator(r'^\d{1,11}$')])
    birthdate =  serializers.CharField()
    gender = serializers.ChoiceField(
                        choices = GENDER_CHOICES)
    email = serializers.CharField(allow_blank=True, allow_null=True, validators=[RegexValidator(r'\b[\w.-]+@[\w.-]+.\w{2,4}\b')])
    avatar = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Profile
        fields =('first_name','last_name','country_code','phone_number','birthdate','gender','email','avatar')
        validators = [
            UniqueTogetherValidator(
                queryset=Profile.objects.all(),
                fields=['phone_number','email']
            )
        ]
    def create(self, validated_data):
        return Profile.objects.create(**validated_data)

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=11,max_length=11, validators=[RegexValidator(r'^\d{1,11}$')])
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    
    class Meta:
        model = User
        fields =('username','password')
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username']
            )
        ]
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data.get('username'),
            email='',
            password=validated_data.get('password')
        )
        user.set_password(validated_data.get('password'))
        user.save()
        return user    

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255, min_length=6, write_only=True)
    username = serializers.CharField(
        max_length=255, min_length=3, write_only=True)
    tokens = serializers.SerializerMethodField()
    def get_tokens(self, obj):
        user = User.objects.get(username=obj['username'])
        token =  Token.objects.get(user=user)
        return {"token":str(token),}

    class Meta:
        model = User
        fields = ['password', 'username','tokens']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        filtered_user_by_username = User.objects.filter(username=username)
        user = auth.authenticate(username=username, password=password)

        
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        
        if not filtered_user_by_username.exists():
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_username[0].auth_provider)

        return {
            'username': user.username,
        }

