from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from language.models import Language
from shared.validators import (
    validate_document_extension,
    validate_image_extension,
    validate_url,
)
from social_media.models import SocialMedia

# Create your models here.

User = get_user_model()


class Person(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='persons'
    )
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, related_name='persons'
    )

    position = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    description = models.TextField()

    avatar = models.ImageField(
        upload_to='avatar/',
        validators=[validate_image_extension],
        blank=True,
    )

    curriculum = models.FileField(
        upload_to='curriculum/',
        validators=[validate_document_extension],
        blank=True,
    )
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.user.first_name} - {self.language.name}'


class SocialAccount(models.Model):
    person = models.ForeignKey(
        Person, models.CASCADE, related_name='person_social_account'
    )
    social_media = models.ForeignKey(
        SocialMedia, models.CASCADE, related_name='person_social_account'
    )
    username = models.CharField(max_length=200)
    url = models.CharField(validators=[validate_url])
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.username} - {self.social_media.name}'
