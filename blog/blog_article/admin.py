from django.contrib import admin

from .models import Blog_article

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('titlt', 'body', 'author', 'publish',
                                                            'status')
admin.site.register(Blog_article, PostAdmin)