from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(
        upload_to="profile", default="profile.jpg", null=True, blank=True)
    display_name = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    options = [
        ("male", "male"), ("female", "female")
    ]
    gender = models.CharField(max_length=50, choices=options, default="male")
    about = models.CharField(max_length=200)


def create_profile(sender, created, instance, **kwargs):
    if created and not instance.is_superuser :
        UserProfile.objects.create(user=instance)


post_save.connect(create_profile,sender=User)
