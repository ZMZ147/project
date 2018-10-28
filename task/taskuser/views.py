from django.shortcuts import render,redirect,reverse
from .forms import *
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password,check_password

from django.http import HttpResponse
from PIL import ImageDraw,ImageFont,Image
import random
from io import BytesIO
# Create your views here.

def test(request):


        return render(request,'base.html',{'username':request.user})

# 注册帐号
def register(request):
    # 思路  点击 注册  回调转到注册表单 get方法  但是 在注册界面 提交 表单应该是注册
    if request.method=='POST':
        submitform=user_register(request.POST)
        # 验证数据
        if submitform.is_valid():
            # 清洗 数据  （巴蜀据全部拿出来）
            cd=submitform.cleaned_data
            if cd['pw1']==cd['pw2']:
                user=UserProfile()
                user.password=make_password(cd['pw1'])
                user.username=cd['username']

                user.save()
                # 登录信息 保存 在 login中
                login(request,user)
                return redirect(reverse('taskuser:test'))

    else:
        user_registrtform=user_register()
        return render(request,'register.html',{'form':user_registrtform})

# 登录 网站
def log_in(request):
    if request.method=='POST':
        form=user_login(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            username=cd['username']
            password=cd['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(reverse('taskuser:test'))

            else:
                return HttpResponse(print(username,password))
        else:
            return HttpResponse(print(form))
    else:
        user_loginform=user_login()
        return render(request,'login.html',{'form':user_loginform})

# 推出登录
def log_out(request):
    logout(request)
    # return redirect(reverse('taskuser:test'))
    return render(request,'base.html')


# 重置密码
def resertpw(request):
    # 注意  虽然是  用的同一个表单 但是 action提交的路径不一样  所以 没什么区别
    if request.method=='POST':
    #     拿到用户
        user=request.user
        form=user_register(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            if cd['pw1']==cd['pw2']:
                user.password=cd['pw1']
                user.save()
                return redirect(reverse('taskuser:test'))
            else:
                return HttpResponse('两次输入的密码不一样')
        else:
            return HttpResponse('请规范输入')
    else:
        user_resertform=user_register()
        return render(request,'register.html',{'form':user_resertform})

    pass

# 注销账户
def zhuxiao_user(request):
    user=request.user
    user.delete()
    logout(request)
    return redirect(reverse('taskuser:test'))




def get_color():
    red = random.randrange(255)
    green=random.randrange(255)
    blue=random.randrange(255)
    return (red,green,blue)

# 实现　　登录验证码的实现
def check_code(request):

#     生成画布
        color=(random.randrange(255),random.randrange(255),random.randrange(255))
        width=100
        height=40
        image=Image.new('RGB',(width,height),color)
# 生成　　画笔

        imagedraw=ImageDraw.Draw(image,'RGB')
        # 默认　　字体　
        fontsize = ImageFont.load_default().font
# 生成　干扰点　防止攻击　１,颜色　　２　范围
        for i in range(500):
            imagedraw.point((random.randrange(width),random.randrange(height)),
                            fill=get_color()
                            # (random.randrange(255),random.randrange(255),random.randrange(255))
                            )
        str='QWERTYUIOPASDFGHJKLZXCVBNM1234567890qwertyuiopasdfghjklzxcvbnm'
        code=''
        # 拿到　　四个　字符串
        for i in range(4):
            code+=str[random.randrange(len(str))]
        print(code)
#         四个字符串　有了　画笔有了　如何写进去？
        for i in range(4):
            imagedraw.text((10+10*i,15),code[i],fill=get_color(),font=fontsize)
        #     将　信息　存到　session中
        request.session['checkcode']=code.lower()
        # 将　所得到的　验证码　存到内存中
        buf=BytesIO()
#
        image.save(buf,'png')
#         返回给前端

        return  HttpResponse(buf.getvalue(),'image/png')

#
# 1. 准备画布
#         size = (100, 40)
#         color = get_color()
#         image = Image.new('RGB', size, color)
#         # 2. 准备画笔
#         imageDraw = ImageDraw.Draw(image, 'RGB')
#         # 3. 设置字体
#         font=ImageFont.load_default().font
#         source = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
#         code = ''
#         # 4. 产生验证码
#         for i in range(4):
#             code += source[random.randrange(len(source))]
#         # 放到session中
#             request.session['code'] = code
#         # 5.将验证码绘制到画布上
#         for i in range(len(code)):
#             imageDraw.text((10 + 18 * i, 10), code[i], fill=get_color(), font=font)
#
#         # 6.干扰点
#         for i in range(500):
#             imageDraw.point((random.randrange(100), random.randrange(40)), fill=get_color())
#
#         buf=BytesIO()
#         image.save(buf, 'png')
#
#         return HttpResponse(buf.getvalue(), 'image/png')









