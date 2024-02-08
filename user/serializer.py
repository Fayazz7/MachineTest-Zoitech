from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import UserProfile


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserProfileSerializer(serializers.ModelSerializer):
    user=serializers.StringRelatedField()
    class Meta:
        model=UserProfile
        fields="__all__"
        read_only_fields=["id","user"]