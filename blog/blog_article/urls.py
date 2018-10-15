from django.conf.urls import url
from blog_article.function import *
urlpatterns=[
    url(r'^1/$',views.test),

    url(r'^2/$',views.get_article),

    url(r'^(?P<post_id>\d+)/share/$',views.post_share,name='post_share'),

]