from django.contrib.auth import get_user_model
from rest_framework import serializers

from connects.models import Connect

User = get_user_model()


class ConnectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Connect
        fields = ['connect_name', 'gamer_tag']




