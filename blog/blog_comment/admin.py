# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment
# Register your models here.

class commentAdmin(admin.ModelAdmin):
    list_display = ['id','name','body']

admin.site.register(Comment,commentAdmin)