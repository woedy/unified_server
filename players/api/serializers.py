
from django.contrib.auth import get_user_model
from rest_framework import serializers

from user_profile.models import UserProfile, GamerTag

User = get_user_model()


class GamerTagSerializers(serializers.ModelSerializer):

    class Meta:
        model = GamerTag
        fields = ['tag_name','console_type']

class ProfileSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['photo', 'position', 'points_per_game', 'assists_per_game', 'rebounds_per_game']


class PlayerSerializers(serializers.ModelSerializer):
    personal_info = ProfileSerializers(many=False)
    user_gamer_tag = GamerTagSerializers(many=True)

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'personal_info', 'user_gamer_tag']

