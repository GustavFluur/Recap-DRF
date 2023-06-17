from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to = 'images/', default= '../default_profile_bhjl12', blank=True
    )
    
    class Meta: 
        ordering = ['-created_at']
    def __str__(self):
        return f'{self.id} {self.title}'
    
