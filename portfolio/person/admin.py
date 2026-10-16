from django.contrib import admin

from .models import Person, SocialAccount

# Register your models here.


class SocialAccountInline(admin.TabularInline):
    model = SocialAccount
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('user', 'language', 'position')
    inlines = (SocialAccountInline,)


@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('person', 'social_media')
