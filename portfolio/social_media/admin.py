from django.contrib import admin

from .models import SocialMedia

# Register your models here.


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('name',)
