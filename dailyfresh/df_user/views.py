from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from . import models
import hashlib
from . import user_decorator


def register(request):
    return render(request, 'df_user/register.html', {"title": '注册'})


def check_uname(request):
    uname = request.GET.get('uname')
    print(uname)
    if models.UserInfo.objects.filter(uname=uname).count() == 1:
        return JsonResponse({"exist": True})
    else:
        return JsonResponse({"exist": False})


def submit(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')

    if upwd != ucpwd:
        return redirect('/user/register/')
    else:
        sha1 = hashlib.sha1()
        sha1.update(upwd.encode('utf-8'))
        upwd = sha1.hexdigest()
        userinfo = models.UserInfo()
        userinfo.uname = uname
        userinfo.upwd = upwd
        userinfo.uemail = uemail
        userinfo.save()
        return redirect('/user/login/')


def login(request):
    username = request.COOKIES.get('username', '')
    print(username)
    return render(request, 'df_user/login.html',
                  {"title": '登录', "error_username": 0, "error_pwd": 0, "username": username})


def logout(request):
    request.session.flush()
    return redirect('/')


def login_handle(request):
    post = request.POST
    username = post.get('username')
    remember = post.get('remember')
    pwd = post.get('pwd')
    sha1 = hashlib.sha1()
    sha1.update(pwd.encode('utf-8'))
    pwd = sha1.hexdigest()
    try:
        item = models.UserInfo.objects.get(uname=username)
    except:
        return render(request, 'df_user/login.html',
                      {"title": '登录', "error_username": 1, "error_pwd": 0, "username": username})
    if item.upwd == pwd:
        request.session['user_id'] = item.id
        request.session['user_name'] = item.uname
        if request.COOKIES.get('url'):
            response = HttpResponseRedirect(request.COOKIES.get('url'))
        else:
            response = HttpResponseRedirect('/user/info/')
        if remember == '1':
            response.set_cookie('username', value=username)
        else:
            response.delete_cookie('username')
        return response
    else:
        return render(request, 'df_user/login.html',
                      {"title": '登录', "error_username": 0, "error_pwd": 1, "username": username})


@user_decorator.login
def info(request):
    user_id = request.session.get('user_id')
    user_name = request.session.get('user_name')
    item = models.UserInfo.objects.get(id=user_id)
    uaddress = item.uaddress
    uphone = item.uphone
    context = {"user_name": user_name, "uaddress": uaddress, "uphone": uphone, "title": '个人信息'}
    return render(request, 'df_user/user_center_info.html', context)


@user_decorator.login
def order(request):
    return render(request, 'df_user/user_center_order.html', {"title": '全部订单'})


@user_decorator.login
def site(request):
    user_id = request.session.get('user_id')
    item = models.UserInfo.objects.get(id=user_id)
    if request.method == "POST":
        item.ushou = request.POST.get('ushou')
        item.uaddress = request.POST.get('uaddress')
        item.uphone = request.POST.get('uphone')
        item.uyoubian = request.POST.get('uyoubian')
        item.save()
        return redirect('/user/site/')
    else:
        ushou = item.ushou
        uaddress = item.uaddress
        uyoubian = item.uyoubian
        uphone = item.uphone
        title = '收货地址'
        context = locals()
        return render(request, 'df_user/user_center_site.html', context)

