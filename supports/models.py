from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()

class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  blank=True, related_name='inquiry_user')
    subject = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField( blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  blank=True, related_name='chat_user')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  blank=True, related_name='chat_admin')
    message = models.TextField( blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
