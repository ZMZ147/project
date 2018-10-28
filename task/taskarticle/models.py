from django.db import models
from datetime import datetime
from taskuser.models import UserProfile
import taggit

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=30, verbose_name='文章类别')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '文章分类'
		verbose_name_plural = verbose_name


class tag(models.Model):
	author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

	tag = models.CharField(max_length=15)

	def __str__(self):
		return self.tag


class ArticleInfo(models.Model):
	title = models.CharField(max_length=50, verbose_name='文章标题')
	desc = models.CharField(max_length=200, verbose_name='文章简介')
	content = models.TextField(verbose_name='文章内容')
	# 评论
	comment_num = models.IntegerField(verbose_name='评论数', default=0)
	# 点击
	click_num = models.IntegerField(verbose_name='点击数', default=0)
	# 点赞 一部夹在
	love_num = models.IntegerField(verbose_name='点赞数', default=0)
	image = models.ImageField(upload_to='article/%y/%m/%d', max_length=120, verbose_name='文章图片')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='发表时间')
	# 关联 了 作者
	author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='文章作者')
	# category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章类别')
	article_tag=models.ManyToManyField(tag)

	# 文章 标签 js函数 达不到预期的效果



	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '文章表'
		verbose_name_plural = verbose_name

# 评论表
class Comment(models.Model):
	article=models.ForeignKey(ArticleInfo,on_delete=models.CASCADE,verbose_name='对应的文章')
	time=models.DateTimeField(default=datetime.now,verbose_name='评论时间')
	content=models.CharField(max_length=200,verbose_name='评论内容')
	author=models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='一个人可以多次评论')





