#from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'user_app'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^login_action/$',views.login_action,name='login_action'),
]