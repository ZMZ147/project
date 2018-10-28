from django.contrib import admin
from .models import ArticleInfo

# Register your models here.
class ArticleInfoAdmin(admin.ModelAdmin):
    model=ArticleInfo
    # 这样定义　貌似页没有用
    search_fields = ['author__username','content']
    list_display = ('title','content','author')

admin.site.register(ArticleInfo,ArticleInfoAdmin)