from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST,HTTP_201_CREATED
from .models import *
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import viewsets


class UserProfileView(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = Profile.objects.all()

class RegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny]


    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        
        user = User.objects.get(username=user_data['username'])
        profile = Profile.objects.create(phone_number=user_data['username'])
        profile.save()
        token =  Token.objects.get_or_create(user=user)[0]
        auth_token = {'auth-token':str(token)}
        return Response(user_data, status=HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=request.data['username'])
        profile = Profile.objects.get(phone_number=request.data['username'])
        response = {
            'token': serializer.data['tokens']['token'],
            'username': str(user),
            'name':str(profile)
        }
        return JsonResponse(response, status=HTTP_200_OK)

