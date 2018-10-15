# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from blog_article.models import Blog_article

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Blog_article, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)