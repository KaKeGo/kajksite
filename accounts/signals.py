from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Profile, User, Friend


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_friend(sender, instance, created, **kwargs):
    if created:
        Friend.objects.create(profile=instance)
