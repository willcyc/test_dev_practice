from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth

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
            print(user)
            print(type(user))
            if user is not None:
                auth.login(request,user)
                return render(request,'user_app/project_manage.html')
            else:
                return render(request,'user_app/index.html',{'error': '用户名或密码错误！'})


