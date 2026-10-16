from rest_framework import serializers

from .models import SocialMedia


class SocialMediaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ('name', 'logo')


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'
