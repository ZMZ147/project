from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime



# auth_user ---> username password email ....
# user django自带的表  user： session ，password加密
# Create your models here.
class UserProfile(AbstractUser):
	nick_name = models.CharField(max_length=20, verbose_name='用户昵称', null=True, blank=True)
	phone = models.CharField(max_length=11, verbose_name='手机号码', null=True, blank=True)
	add_time = models.DateTimeField(default=datetime.now, verbose_name='注册时间')



	def __str__(self):
		return self.username

	class Meta:
		verbose_name = '用户信息'
		verbose_name_plural = verbose_name
