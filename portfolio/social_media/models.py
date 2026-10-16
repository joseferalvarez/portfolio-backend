from django.db import models
from django.utils import timezone

from shared.validators import validate_vector_extension

# Create your models here.


class SocialMedia(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.FileField(
        upload_to='socialmedia/',
        validators=[validate_vector_extension],
        blank=True,
    )
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Social media'
        verbose_name_plural = 'Social medias'

    def __str__(self):
        return self.name
