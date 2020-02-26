# login/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from mainWindow.models import House
from . import models
from .forms import UserForm
from .forms import RegisterForm
from .forms import ChangeForm
from .models import User

# 作者：王皓平 创建时间：2019.8.27 最后更新时间：2019.9.10
def index(request):
    city_info = request.POST.get('city_Info')
    if request.method == "POST":
        if city_info == '南京':
            return redirect("indexnj.html")
        elif city_info == '成都':
            return redirect("indexcd.html")
        elif city_info == '长沙':
            return redirect("indexcs.html")
        elif city_info == '广州':
            return redirect("indexgz.html")
        elif city_info == '杭州':
            return redirect("indexhz.html")
        elif city_info == '南昌':
            return redirect("indexnc.html")
        elif city_info == '上海':
            return redirect("indexsh.html")
        elif city_info == '苏州':
            return redirect("indexsu.html")
        elif city_info == '深圳':
            return redirect("indexsz.html")
        elif city_info == '天津':
            return redirect("indextj.html")
        elif city_info == '太原':
            return redirect("indexty.html")
        elif city_info == '武汉':
            return redirect("indexwh.html")
        elif city_info == '无锡':
            return redirect("indexwx.html")
        elif city_info == '北京':
            return redirect("indexbj.html")
        else:
            return render(request, "index1.html", locals())
    return render(request, "index1.html", locals())


def login(request):
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            phone = register_form.cleaned_data['phone']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.phone= phone
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/")

def information(request):
    user = models.User.objects.get(id = request.session['user_id'])
    username = user.name
    return render(request,'login/information.html',locals())

def edit(request):
    user = models.User.objects.get(id = request.session['user_id'])
    if request.method == "POST":
        change_form = ChangeForm(request.POST)
        if change_form.is_valid():
            em = change_form.cleaned_data['new_email']
            if em != user.email:
                same_email_user = models.User.objects.filter(email=em)
                if same_email_user:
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/edit.html', locals())
                else:
                    user.email = em
            else:
                user.email = em

            ph = change_form.cleaned_data['new_phone']
            user.phone = ph
            user.save()
            return redirect('/information/')

    change_form = ChangeForm(initial={"new_email":user.email,"new_phone":user.phone})
    return render(request, 'login/edit.html', locals())




def Hcompare(request):
    roomType1 = House.objects.filter(wkind="住宅")
    roomType2 = House.objects.filter(wkind="别墅")
    roomType3 = House.objects.filter(wkind="写字楼")
    roomType4 = House.objects.filter(wkind="底商")
    roomType5 = House.objects.filter(wkind="酒店式公寓")
    s1=s2=s3=s4=s5=0
    for sr1 in roomType1:
        s1+=1
    for sr2 in roomType2:
        s2+=1
    for sr3 in roomType3:
        s3+=1
    for sr4 in roomType4:
        s4+=1
    for sr5 in roomType5:
        s5+=1


    return render(request,'compare.html',locals())

def userInfo(request):
    return render(request,'userInfo.html',locals())


