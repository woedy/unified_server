from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  blank=True, related_name='memberships')
    membership_type = models.CharField(max_length=255, blank=True, null=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
