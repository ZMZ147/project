#-*- coding: UTF-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from ..forms import *
from ..models import *
from blog_comment.forms import *

from django.core.mail import send_mail

# Create your views here.


def test(request):
    return render(request,'mainPage.html')

# 下面 的是 从 数据库  拿到 文章 的 方法
def get_article(request):
    articles=Blog_article.objects.all().values()
    comment=Comment.objects.values()
    print('1')

    print(articles)

    return render(request,'mainPage.html',{'articles':articles,
                                           'comment':comment})




# z这 是 关于邮件分享的view函数
def post_share(request, post_id):
# retrieve post by id
    post = get_object_or_404(Blog_article, id=post_id, status='published')
    if request.method == 'POST':
# Form was submitted
        form = Email(request.POST)
        if form.is_valid():

            cd = form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject='{},{}  you reading{}'.format( cd['name'],cd['mail'],post.title)
            message='{}'.format(cd['content'])
            send_mail(subject,message,'1144569792@qq.com',[cd['to']])
            send=True
    else:
        form = Email()
#     return render(request, 'blog/post/share.html', {'post': post,
# 'form': form,'send':send})
    return HttpResponse('nihao a')




def post_detail(request, year, month, day, post):
    post = get_object_or_404(Blog_article, slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)
# List of active comments for this post
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
# A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
# Create Comment object but don't save to database yet   保存 但是没有提交到数据库
            new_comment = comment_form.save(commit=False)
# Assign the current post to the comment 让两者进行关联
            new_comment.post = post
# Save the comment to the database  这里才真正保存到数据库
            new_comment.save()
    else:
        comment_form = CommentForm()
    # return render(request,
    #                     'blog/post/detail.html',
    #                                             {'post': post,
    #                                             'comments': comments,
    #                                             'new_comment': new_comment,
    #                                             'comment_form': comment_form})
    return HttpResponse('nihao')