from django.shortcuts import render,redirect,reverse,HttpResponse
from .forms import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.

# 封装一个认证函数

# 展示 用户的个人界面
def show(request):

    # 拿到用户的所有文章
    article_list=ArticleInfo.objects.filter(author=request.user)
    #    分页 共能  实现分页器
    paginator=Paginator(article_list,6)
    # 拿到 第几页 如果 没有 默认为一
    page=request.GET.get('page',1)

    try:
        list=paginator.page(page)
    except PageNotAnInteger:
        # 如果  页数  超过 最大值 那么 默认返回最后一页
        list=paginator.page(paginator.num_pages)
    except EmptyPage:
        # 如果输入的  是空的  那么  默认 返回的是第一页
        list=paginator.page(1)


    return render(request,'user/user_index.html',{'username':request.user,'list':list})

# 发表文章
@login_required()
def add_article(request):
    if request.method=='POST':
        form=articleform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
    #         能不能直接将得到的数据 提交到类里面  尝试过了  不行
            article=ArticleInfo()
            article.title=cd['title']
            article.content=cd['content']
            article.author=request.user

            article.save()
            return redirect(reverse('taskarticle:show'))

    else:
        form=articleform()
        tag=tagform()
        return render(request,'user/add_article.html',{'form':form,'username':request.user,'tagform':tag})

# 查看文章/评论 我一起写了
def get_article(request):
#     拿到文章id
    if request.method=='GET':
        id=request.GET.get('id')
        article=ArticleInfo.objects.get(id=id)
    #     每次点击这篇文章  浏览次数+1
        article.click_num+=1
        article.save()
    #     生成 一个 评论表单
        comment=commentform()
    #     将 拿到的这篇文章 渲染啊
        return render(request,'user/check_article.html',{'article':article,
                                                         'form':comment,
                                                         'username':request.user})
    else:
        # 先 将 评论的 内容 保存到数据库

        com=commentform(request.POST)
        if com.is_valid():
            cd=com.cleaned_data
            id=request.GET.get('id')
            print(id)
            article = ArticleInfo.objects.get(id=id)
            new_com=Comment()
            new_com.article=article
            new_com.content=cd['content']
            new_com.author=request.user
            new_com.save()

            # return redirect(reverse('taskarticle:get',args=[id]))
            # 生成 一个 评论表单
            comment=commentform()
        #     将 拿到的这篇文章 渲染啊
            return render(request,'user/check_article.html',{'article':article,
                                                             'form':comment,
                                                             'username':request.user})




# 更新文章
def update_article(request):
    pass

# 删除文章
def delete_article(request):
    pass

# 点赞  功能 （异步）
def dianzan(request):
#     拿到文章id

    print('过得来么')
    id=request.GET.get('id')
    print(id)
    article=ArticleInfo.objects.get(id=id)

#     点赞
    article.love_num+=1
    data=article.love_num
    print(data)
    article.save()
    # 返回点咱书

    return HttpResponse(data)


# 实现  站内搜索  这样就没有使用 haystack内置的搜索功能！
def search(request):
        # 拿到  关键词
        q = request.GET.get('q')
        print(q)
        # 拿到 所有的 标题 作者 或者 内容
        # Related Field got invalid lookup: icontains  出现这种 错误
        post_list = ArticleInfo.objects.filter(Q(title__icontains=q) | Q(author__icontains=q)
                                               | Q(content__icontains=q))


        # invalid literal for int() with base 10: 'my' 出现这种错误
        # post_list = ArticleInfo.objects.filter(author=q)

        if post_list.count()== 0  :
            print(1111)
            return redirect(reverse('global_search'))


        else:

            return render(request, 'search/search.html', {'articles': post_list})



def test_article(request):
    article_test=ArticleInfo.objects.filter(Q(content__icontains='s')|Q(author__icontains='m'))
    # article_test=ArticleInfo.objects.filter(author__icontains='m')
    # article_test = ArticleInfo.objects.filter(content__icontains='s')
    return render(request,'test.html',{'articles':article_test})


from haystack.views import SearchView