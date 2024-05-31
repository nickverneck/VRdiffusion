from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Video

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('vr_peripheral',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Video)
