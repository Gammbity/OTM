from django.contrib import admin
from .models import StudentModel, TypeModel, OtmModel, AddSponsorModel

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['id', 'full_name']
    readonly_fields = ['allocated_amount']

@admin.register(AddSponsorModel)
class AddSponsorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_sponsor_full_name']
    list_display_links = ['id', 'get_sponsor_full_name']

@admin.register(TypeModel)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    
@admin.register(OtmModel)
class OtmAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

