from django.contrib import admin

from django.contrib.auth import get_user_model

CustomUser = get_user_model()


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username', 'user_type', 'created_at']
    list_filter = ['created_at']
    date_hierarchy = 'created_at'
    ordering = ['email']
