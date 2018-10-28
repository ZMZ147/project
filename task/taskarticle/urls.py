from django.urls import path
from taskarticle.views import *

urlpatterns=[

    path('',show,name='show'),

    path('add',add_article,name='add'),

    path('get',get_article,name='get'),

    path('update',update_article,name='update'),

    path('delete',delete_article,name='delete'),


    path('dianzan',dianzan,name='dianzan'),


    path('search',search,name='search'),


    path('test',test_article,name='test'),



]