from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=300. bank=True)
    content = models.TextField(blank=True)
    image = models.ImageField (
        upload_to='images/', default='../default_profile_bhjl12'
    )

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}'s profile"
        

def create_profile(sender, created, **kwargs):
    if created: 
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)