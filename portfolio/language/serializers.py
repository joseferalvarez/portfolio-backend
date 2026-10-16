from rest_framework import serializers

from .models import Language


class LanguageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('name', 'iso')


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
