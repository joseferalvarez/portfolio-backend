from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from language.models import Language

# Create your models here.

User = get_user_model()


# TODO: add validators for pdf and image files


class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='persons')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='persons')

    position = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    description = models.TextField()

    avatar = models.ImageField(
        upload_to='avatar/',
        blank=True,
    )

    curriculum = models.FileField(
        upload_to='curriculum/',
        blank=True,
    )

    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.user.first_name} - {self.language.name}'
