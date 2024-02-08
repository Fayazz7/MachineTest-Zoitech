from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import serializers

from user.serializer import RegistrationSerializer,UserProfileSerializer
from user.models import UserProfile
# Create your views here.

class RegistrationView(APIView):
    def post(self,request,*args, **kwargs):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (data=serializer.data)
        else:
            return Response (data=serializer.errors)
        
class UserProfileView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]   
    def update(self,request,*args, **kwargs):
        user_obj=request.user.profile
        user_obj_id=request.user.profile.user_id
        if user_obj_id == int(kwargs.get("pk")):
            serializer=UserProfileSerializer(data=request.data,instance=user_obj)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response (data=serializer.data)
            else:
                return Response (data=serializer.errors)
        else:
            raise serializers.ValidationError ("Permission Denied")
        
    def retrieve(self,request,*args, **kwargs):
        user_object=request.user.profile
        if request.user.id == int(kwargs.get("pk")):
            serializer=UserProfileSerializer(instance=user_object)
            return Response (data=serializer.data)
        else:
            raise serializers.ValidationError("Permission Needed")