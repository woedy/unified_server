import os
import random

from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL




CONNECT_CHOICES = (
    ("PSN", "PSN"),
    ("Xbox Live", "Xbox Live"),
    ("Twitter", "Twitter"),
    ("Discord", "Discord"),
    ("Twitch", "Twitch"),
)

class Connect(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_connects')

    connect_name = models.CharField(choices=CONNECT_CHOICES, max_length=255, blank=True, null=True)
    gamer_tag = models.CharField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return self.connect_name
