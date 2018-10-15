from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Blog_article(models.Model):
    titlt=models.CharField(max_length=30)
    body=models.TextField()
    author=models.ForeignKey(User,related_name='name')
    create_time=models.DateTimeField(auto_created=True)
    update_time=models.DateTimeField(auto_now_add=True)
    publish=models.DateTimeField(timezone.now())
    status=(
        ('drafit','Drafit'),
        ('published','Published')
    )

    class Meta:

        ordering=('publish',)

    def __str__(self):
        return self.titlt


