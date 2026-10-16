from django.db import models
from django.utils import timezone

from shared.validators import validate_image_extension, validate_url
from social_media.models import SocialMedia

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=300, unique=True)
    webpage = models.CharField(validators=[validate_url])
    logo = models.ImageField(
        upload_to='company/',
        validators=[validate_image_extension],
        blank=True,
    )
    created_at = models.DateField(timezone.now)
    updated_at = models.DateField(timezone.now)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class CompanySocialAccount(models.Model):
    company = models.ForeignKey(
        Company, models.CASCADE, related_name='company_social_account'
    )
    social_media = models.ForeignKey(
        SocialMedia, models.CASCADE, related_name='company_social_account'
    )
    username = models.CharField(max_length=200)
    url = models.CharField(validators=[validate_url])
    created_at = models.DateField(default=timezone.now)
    updated_at = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = 'Company social account'
        verbose_name_plural = 'Company social accounts'

    def __str__(self):
        return f'{self.company} - {self.social_media}'
