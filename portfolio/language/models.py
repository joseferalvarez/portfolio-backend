from django.db import models
from django.utils import timezone

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=20)
    iso = models.CharField(max_length=2)
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name
