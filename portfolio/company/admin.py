from django.contrib import admin

from .models import Company, CompanySocialAccount

# Register your models here.


class CompanySocialAccountInline(admin.TabularInline):
    model = CompanySocialAccount
    extra = 1


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = (CompanySocialAccountInline,)


@admin.register(CompanySocialAccount)
class CompanySocialAccountAdmin(admin.ModelAdmin):
    list_display = ('company', 'social_media')
