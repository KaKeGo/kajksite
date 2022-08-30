from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'user', 'user', 'avatar', 'bio', 'first_name', 'last_name',
            'friends', 'slug', 'get_username', 'get_full_name'
        ]
