from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from enum import IntEnum


class UserRole(IntEnum):
    Player = 0
    Developer = 1

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=1,
        choices=[(role.value, role.name) for role in UserRole],
        default='',
    )
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + " - " + self.role

    @property
    def is_player(self):
        return int(self.role) == UserRole.Player.value

    @property
    def is_developer(self):
        return int(self.role) == UserRole.Developer.value

    @property
    def username(self):
        return self.user.username

    @staticmethod
    def get_user_profile_or_none(user):
        if not user.is_authenticated:
            return None
        try:
            return UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            return None

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()