from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    VR_PERIPHERAL_CHOICES = [
        ('Meta Quest 2', 'Meta Quest 2'),
        ('Meta Quest 3', 'Meta Quest 3'),
        ('Apple Vision Pro', 'Apple Vision Pro'),
    ]
    
    vr_peripheral = models.CharField(max_length=50, choices=VR_PERIPHERAL_CHOICES)

class Video(models.Model):
    VIDEO_TYPE_CHOICES = [
        ('180', '180 Degrees'),
        ('360', '360 Degrees'),
    ]
    
    PRIVACY_CHOICES = [
        ('private', 'Private'),
        ('public', 'Public'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_type = models.CharField(max_length=3, choices=VIDEO_TYPE_CHOICES)
    privacy = models.CharField(max_length=7, choices=PRIVACY_CHOICES)
    video_file = models.FileField(upload_to='videos/')
    upload_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'video')
