from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Video, Like
from django.contrib.auth import get_user_model
from .serializers import VideoSerializer, LikeSerializer, CustomUserSerializer

# Get the User model
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeVideoView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, video_id):
        video = generics.get_object_or_404(Video, id=video_id)
        like, created = Like.objects.get_or_create(user=request.user, video=video)
        if not created:
            return Response({'detail': 'You have already liked this video.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Video liked successfully.'}, status=status.HTTP_201_CREATED)
    
    def delete(self, request, video_id):
        video = generics.get_object_or_404(Video, id=video_id)
        like = generics.get_object_or_404(Like, user=request.user, video=video)
        like.delete()
        return Response({'detail': 'Like removed successfully.'}, status=status.HTTP_204_NO_CONTENT)
