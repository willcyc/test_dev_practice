from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'user_app/index.html')

#处理登录
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "" or password == "":
            return render(request, 'user_app/index.html', {'error': '用户名或密码不能为空！'})

        else:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                #response = HttpResponseRedirect('/project_manage/')
                #response.set_cookie('user',username,3600)
                #return response
                request.session['user'] = username
                return HttpResponseRedirect('/project_manage/')
            else:
                return render(request,'user_app/index.html',{'error': '用户名或密码错误！'})
    else:
        return render(request,'user_app/index.html')

@login_required
def project_manage(request):
    #username = request.COOKIES.get('user','')
    username = request.session.get('user','')
    return render(request,'user_app/project_manage.html',{'user':username})

def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/')
    return response