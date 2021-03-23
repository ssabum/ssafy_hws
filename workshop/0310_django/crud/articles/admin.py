from django.contrib import admin
from .models import Article

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'created_at',
        'updated_at',
    )

admin.site.register(Article, PostAdmin)