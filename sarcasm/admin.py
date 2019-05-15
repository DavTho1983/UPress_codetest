from django.contrib import admin
from .models import Headline


@admin.register(Headline)
class HeadlineAdmin(admin.ModelAdmin):
    list_display = (
        "article_link",
        "headline",
        "is_sarcastic",
    )
    ordering = ["id"]
