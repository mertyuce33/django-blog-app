from django.contrib import admin

# Register your models here.

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['name','surname','email']
    list_display_links=['name']
    search_fields=['name']
    list_filter=['name']
    class Meta:
        model=Profile
