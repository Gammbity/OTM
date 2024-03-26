from django.contrib import admin
from .models import SponsorModel, ConditionModel, IsHumanModel

@admin.register(SponsorModel)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['id', 'full_name']
    readonly_fields = ['use_value']

@admin.register(ConditionModel)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

@admin.register(IsHumanModel)
class IsHumanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

