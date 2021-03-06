# Generated by Django 2.1.2 on 2018-10-24 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('desc', models.CharField(max_length=200, verbose_name='文章简介')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('comment_num', models.IntegerField(default=0, verbose_name='评论数')),
                ('click_num', models.IntegerField(default=0, verbose_name='点击数')),
                ('love_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('image', models.ImageField(max_length=120, upload_to='article/%y/%m/%d', verbose_name='文章图片')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间')),
            ],
            options={
                'verbose_name': '文章表',
                'verbose_name_plural': '文章表',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='文章类别')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
            },
        ),
    ]
