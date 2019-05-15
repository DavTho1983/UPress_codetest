from django.contrib import admin
from .models import User

@admin.register(User)
class LondonWeatherAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "is_active",
        "is_staff",
    )
    ordering = ["id"]