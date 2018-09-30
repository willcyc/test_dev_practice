#from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'user_app'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login_action/$',views.login_action,name='login_action'),
    url(r'^project_manage/$',views.project_manage,name='project_manage'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'accounts/login/$',views.index,name='index'),
]