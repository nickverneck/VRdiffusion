from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Video, Like

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'vr_peripheral']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'video', 'created_at']
        read_only_fields = ['created_at']

class VideoSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = '__all__'
        read_only_fields = ['user', 'upload_date']

    def get_likes_count(self, obj):
        return obj.likes.count()