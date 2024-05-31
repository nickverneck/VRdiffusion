from django.urls import path
from .views import RegisterView, VideoListCreateView, LikeVideoView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('videos/', VideoListCreateView.as_view(), name='video-list-create'),
    path('videos/<int:video_id>/like/', LikeVideoView.as_view(), name='like-video'),
]