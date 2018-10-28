from django.urls import path
from taskuser.views import *
urlpatterns=[
    path('',test,name='test'),

    path('login',log_in,name='login'),

    path('register',register,name='register'),

    path('resertpw',resertpw,name='resertpw'),
    # 注销 帐 号
    path('zhuxiao_user',zhuxiao_user,name='quit'),

    path('logout',log_out,name='logout'),

    path('check_code',check_code,name='check_code')

]